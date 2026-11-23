import time
from config import BOT_NAME, OWNER_NAME, PREFIX

def handle_general_commands(client, message, text):
    if text == f"{PREFIX}ping":
        start_time = time.time()
        client.reply_message("جاري الفحص... ⏳", message)
        speed = round((time.time() - start_time) * 1000, 2)
        client.reply_message(f"🚀 *سرعة الاستجابة:* {speed} ms", message)
        return True

    elif text in [f"{PREFIX}menu", f"{PREFIX}اوامر"]:
        menu_text = f"""
🤖 *قائمة أوامر {BOT_NAME}*
👑 *المطور:* {OWNER_NAME}

📌 *الأوامر العامة:*
• `{PREFIX}ping` - فحص سرعة البوت
• `{PREFIX}info` - معلومات البوت

👥 *أوامر المجموعات:*
• `{PREFIX}رابط` - جلب رابط المجموعة
• `{PREFIX}معلومات_المجموعة` - إحصائيات المجموعة

🛠️ *الأدوات والألعاب:*
• `{PREFIX}حكمة` - اقتباس عشوائي
• `{PREFIX}احسب [عملية]` - آلة حاسبة (مثال: `{PREFIX}احسب 5*10`)
• `{PREFIX}العب [حجر/ورقة/مقص]` - لعبة سريعة

👑 *أوامر المطور (خاصة):*
• `{PREFIX}المطور` - فحص الصلاحية
• `{PREFIX}restart` - إعادة تشغيل البوت
• `{PREFIX}stop` - إيقاف البوت
        """
        client.reply_message(menu_text.strip(), message)
        return True

    elif text == f"{PREFIX}info":
        client.reply_message(f"⚡ *{BOT_NAME}*\nيعمل بلغة Python على بيئة Termux.", message)
        return True

    return False
    
