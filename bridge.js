طconst { default: makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion } = require('@whiskeysockets/baileys');
const pino = require('pino');
const { spawnSync, exec } = require('child_process');
const fs = require('fs');

const BOT_NUMBER = "212784776925";

async function startBridge() {
    const { state, saveCreds } = await useMultiFileAuthState('session');
    const { version } = await fetchLatestBaileysVersion();

    const sock = makeWASocket({
        version,
        logger: pino({ level: 'silent' }),
        auth: state,
        browser: ["Ubuntu", "Chrome", "20.0.04"]
    });

    if (!sock.authState.creds.registered) {
        setTimeout(async () => {
            let code = await sock.requestPairingCode(BOT_NUMBER);
            code = code?.match(/.{1,4}/g)?.join("-") || code;
            console.log(`\n==========================================`);
            console.log(`🔑 كود تفعيل البوت للرقم (${BOT_NUMBER}): ${code}`);
            console.log(`==========================================\n`);
        }, 3000);
    }

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        if (update.connection === 'open') {
            console.log(`\n✅ تم ربط جميع الأقسام بنجاح! البوت جاهز 🐍\n`);
        } else if (update.connection === 'close') {
            startBridge();
        }
    });

    sock.ev.on('messages.upsert', async (chatUpdate) => {
        const msg = chatUpdate.messages.at(0);
        if (!msg || !msg.message) return;

        const m = msg.message;
        const text = m.conversation || 
                     (m.extendedTextMessage && m.extendedTextMessage.text) || 
                     (m.imageMessage && m.imageMessage.caption) || "";

        if (!text || !text.startsWith(".")) return;

        const from = msg.key.remoteJid;
        const isGroup = from.endsWith("@g.us");
        const sender = msg.key.participant || from;
        const quotedSender = m.extendedTextMessage?.contextInfo?.participant || "";

        console.log(`📩 أمر مستلم: ${text}`);

        const payload = JSON.stringify({ from, sender, text, isGroup, quotedSender });
        const py = spawnSync('python3', ['bot.py', payload], { encoding: 'utf-8' });

        if (py.stderr) console.error(`⚠️ خطأ في بايثون:\n${py.stderr}`);
        if (!py.stdout || !py.stdout.trim()) return;

        const output = py.stdout.trim();

        // 1. إرسال صورة
        if (output.startsWith("IMAGE|")) {
            const parts = output.split("|");
            const imageUrl = parts.at(1);
            const captionText = parts.slice(2).join("|");
            try {
                const res = await fetch(imageUrl, { headers: { "User-Agent": "Mozilla/5.0" } });
                const buf = Buffer.from(await res.arrayBuffer());
                await sock.sendMessage(from, { image: buf, caption: captionText }, { quoted: msg });
            } catch {
                await sock.sendMessage(from, { text: captionText }, { quoted: msg });
            }
        }
        // 2. إجراءات المجموعات
        else if (output.startsWith("GROUP_ACTION|")) {
            const [, action, param] = output.split("|");
            try {
                if (action === "close") {
                    await sock.groupSettingUpdate(from, 'announcement');
                    await sock.sendMessage(from, { text: param }, { quoted: msg });
                } else if (action === "open") {
                    await sock.groupSettingUpdate(from, 'not_announcement');
                    await sock.sendMessage(from, { text: param }, { quoted: msg });
                } else if (action === "link") {
                    const code = await sock.groupInviteCode(from);
                    await sock.sendMessage(from, { text: `${param}\nhttps://whatsapp.com{code}` }, { quoted: msg });
                } else if (action === "info") {
                    const meta = await sock.groupMetadata(from);
                    await sock.sendMessage(from, { text: `${param}\n• الاسم: ${meta.subject}\n• الأعضاء: ${meta.participants.length}` }, { quoted: msg });
                } else if (action === "tagall") {
                    const meta = await sock.groupMetadata(from);
                    const mentions = meta.participants.map(p => p.id);
                    await sock.sendMessage(from, { text: `📢 *منشن جماعي:*\n${param}`, mentions }, { quoted: msg });
                } else if (action === "promote") {
                    await sock.groupParticipantsUpdate(from, [param], "promote");
                    await sock.sendMessage(from, { text: "⬆️ تم ترقية العضو إلى مشرف بنجاح." }, { quoted: msg });
                } else if (action === "demote") {
                    await sock.groupParticipantsUpdate(from, [param], "demote");
                    await sock.sendMessage(from, { text: "⬇️ تم تخفيض رتبة المشرف." }, { quoted: msg });
                } else if (action === "kick") {
                    await sock.groupParticipantsUpdate(from, [param], "remove");
                    await sock.sendMessage(from, { text: "👢 تم طرد العضو من المجموعة." }, { quoted: msg });
                }
            } catch (e) {
                await sock.sendMessage(from, { text: "❌ فشل التنفيذ. تأكد أن البوت مشرف (Admin) في المجموعة." }, { quoted: msg });
            }
        }
        // 3. تحميل الصوتيات عبر yt-dlp
        else if (output.startsWith("DOWNLOAD_AUDIO|")) {
            const query = output.split("|").at(1);
            await sock.sendMessage(from, { text: `⏳ جاري البحث وتحميل الصوت: *${query}*...` }, { quoted: msg });
            const outFile = `temp_audio_${Date.now()}.mp3`;
            const cmd = query.startsWith("http") ? `yt-dlp -x --audio-format mp3 -o "${outFile}" "${query}"` : `yt-dlp -x --audio-format mp3 -o "${outFile}" "ytsearch1:${query}"`;
            exec(cmd, async (err) => {
                if (!err && fs.existsSync(outFile)) {
                    await sock.sendMessage(from, { audio: fs.readFileSync(outFile), mimetype: 'audio/mp4' }, { quoted: msg });
                    fs.unlinkSync(outFile);
                } else {
                    await sock.sendMessage(from, { text: "❌ فشل التحميل. تأكد من تثبيت yt-dlp و ffmpeg في Termux." }, { quoted: msg });
                }
            });
        }
        // 4. أوامر المطور (تحديث وإعادة تشغيل)
        else if (output.startsWith("OWNER_ACTION|restart")) {
            await sock.sendMessage(from, { text: "🔄 جاري سحب التحديثات وإعادة تشغيل البوت..." }, { quoted: msg });
            exec("git pull", () => process.exit(0));
        }
        // 5. رد نصي عادي
        else {
            await sock.sendMessage(from, { text: output }, { quoted: msg });
        }
    });
}

startBridge();
            
