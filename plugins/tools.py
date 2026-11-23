from config import BOT_NAME, OWNER_NAME, PREFIX

def handle_general(text):
    if text == f"{PREFIX}ping":
        return "🚀 *سرعة الاستجابة:* البوت يعمل بكفاءة عالية (Python 🐍)!"
    
    elif text in [f"{PREFIX}menu", f"{PREFIX}اوامر"]:
        return f"""🤖 *قائمة أوامر {BOT_NAME}*
👑 *المطور:* {OWNER_NAME}

📌 *الأوامر العامة:*
• `{PREFIX}ping` - فحص سرعة البوت
• `{PREFIX}info` - معلومات البوت
• `{PREFIX}المطور` - فحص صلاحية المطور

🛠️ *الأدوات والألعاب (Python):*
• `{PREFIX}حكمة` - اقتباس عشوائي
• `{PREFIX}احسب [عملية]` - آلة حاسبة (مثال: `{PREFIX}احسب 5*10`)
• `{PREFIX}العب [حجر/ورقة/مقص]` - لعبة سريعة"""

    elif text == f"{PREFIX}info":
        return f"⚡ *{BOT_NAME}*\nمبرمج بلغة Python 🐍 ويعمل على Termux."

    return None
    
