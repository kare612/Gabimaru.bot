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
            console.log(`\n✅ تم ربط الجسر بنجاح! البوت يعمل الآن بمحرك Python 🐍\n`);
        } else if (update.connection === 'close') {
            startBridge();
        }
    });

    sock.ev.on('messages.upsert', async ({ messages }) => {
        const msg = messages[0];
        if (!msg.message || msg.key.fromMe) return;

        const from = msg.key.remoteJid;
        const sender = msg.key.participant || from;
        const text = msg.message.conversation || msg.message.extendedTextMessage?.text || "";

        if (!text) return;

        // تمرير الرسالة إلى ملف bot.py بلغة بايثون
        const payload = JSON.stringify({ from, sender, text });
        const py = spawnSync('python3', ['bot.py', payload], { encoding: 'utf-8' });

        if (py.stdout && py.stdout.trim()) {
            await sock.sendMessage(from, { text: py.stdout.trim() }, { quoted: msg });
        }
    });
}

startBridge();
      
