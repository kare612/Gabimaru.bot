const { default: makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion } = require('@whiskeysockets/baileys');
const pino = require('pino');
const { spawnSync } = require('child_process');

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
            console.log(`\n✅ تم ربط الجسر بنجاح! البوت جاهز لاستقبال الأوامر 🐍\n`);
        } else if (update.connection === 'close') {
            startBridge();
        }
    });

    sock.ev.on('messages.upsert', async (chatUpdate) => {
        const msg = chatUpdate.messages.at(0);
        if (!msg || !msg.message) return;

        // استخراج النص من جميع أنواع الرسائل
        const m = msg.message;
        const text = m.conversation || 
                     (m.extendedTextMessage && m.extendedTextMessage.text) || 
                     (m.imageMessage && m.imageMessage.caption) || "";

        if (!text || !text.startsWith(".")) return;

        const from = msg.key.remoteJid;
        const sender = msg.key.participant || from;

        console.log(`📩 أمر مستلم: ${text}`);

        // تمرير البيانات إلى بايثون
        const payload = JSON.stringify({ from, sender, text });
        const py = spawnSync('python3', ['bot.py', payload], { encoding: 'utf-8' });

        if (py.stderr) {
            console.error(`⚠️ خطأ في بايثون:\n${py.stderr}`);
        }

        if (py.stdout && py.stdout.trim()) {
            await sock.sendMessage(from, { text: py.stdout.trim() }, { quoted: msg });
            console.log(`✅ تم إرسال الرد بنجاح!`);
        }
    });
}

startBridge();
                                         
