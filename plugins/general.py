from config import BOT_NAME, OWNER_NAME, PREFIX

def handle_general(text):
    cmd = text.lower()
    
    if cmd == f"{PREFIX}ping" or cmd == f"{PREFIX}بنج":
        return "⚡ *سرعة الاستجابة:* البوت يعمل بكفاءة عالية (Python 🐍)!"
    
    elif cmd in [f"{PREFIX}menu", f"{PREFIX}اوامر", f"{PREFIX}الاوامر", f"{PREFIX}بوت"]:
        return f"""╔══════════════════╗
🔥 *{BOT_NAME}* 🔥
╚══════════════════╝
👑 *المطور:* {OWNER_NAME}

╭─ 📌 *الأوامر العامة*
│ ✦ `{PREFIX}بنج` - فحص سرعة البوت
│ ✦ `{PREFIX}معلومات` - معلومات البوت
╰────────────────

╭─ 🛠️ *الأدوات والترفيه*
│ ✦ `{PREFIX}حكمة` - اقتباس أنمي عشوائي
│ ✦ `{PREFIX}ذكر` - أذكار إسلامية
│ ✦ `{PREFIX}احسب [عملية]` - آلة حاسبة (مثال: `{PREFIX}احسب 5*10`)
│ ✦ `{PREFIX}العب` - لعبة حجر ورقة مقص
│ ✦ `{PREFIX}زخرفة [نص]` - زخرفة النصوص العربية
╰────────────────"""

    elif cmd in [f"{PREFIX}info", f"{PREFIX}معلومات"]:
        return f"⚡ *{BOT_NAME}*\nمبرمج بلغة Python 🐍 ومتصل عبر كود الاقتران."

    return None
