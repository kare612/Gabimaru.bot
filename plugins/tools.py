import random
from config import PREFIX

QUOTES = [
    "النجاح هو الانتقال من فشل إلى فشل دون فقدان الحماس.",
    "لا تؤجل عمل اليوم إلى الغد.",
    "البرمجة ليست مجرد كتابة كود، بل هي فن حل المشكلات.",
    "العلم نور والجهل ظلام."
]

def handle_tools_commands(client, message, text):
    # أمر اقتباس عشوائي
    if text in [f"{PREFIX}حكمة", f"{PREFIX}quote"]:
        quote = random.choice(QUOTES)
        client.reply_message(f"💡 *حكمة اليوم:*\n_{quote}_", message)
        return True

    # أمر حجر ورقة مقص
    elif text.startswith(f"{PREFIX}العب "):
        user_choice = text.replace(f"{PREFIX}العب ", "").strip()
        choices = ["حجر", "ورقة", "مقص"]
        if user_choice not in choices:
            client.reply_message(f"⚠️ اختر واحداً: `{PREFIX}العب حجر` أو `ورقة` أو `مقص`", message)
            return True
        
        bot_choice = random.choice(choices)
        if user_choice == bot_choice:
            result = "تعادل! 🤝"
        elif (user_choice == "حجر" and bot_choice == "مقص") or \
             (user_choice == "ورقة" and bot_choice == "حجر") or \
             (user_choice == "مقص" and bot_choice == "ورقة"):
            result = "أنت فزت! 🎉"
        else:
            result = "البوت فاز! 🤖"

        client.reply_message(f"👤 اختيارك: *{user_choice}*\n🤖 اختيار البوت: *{bot_choice}*\n\n🏆 النتيجة: *{result}*", message)
        return True

    # أمر آلة حاسبة بسيطة (مثال: .احسب 50 + 25)
    elif text.startswith(f"{PREFIX}احسب "):
        expression = text.replace(f"{PREFIX}احسب ", "").strip()
        # السماح بالأرقام والعمليات الحسابية الأساسية فقط للأمان
        allowed_chars = "0123456789+-*/(). "
        if all(c in allowed_chars for c in expression):
            try:
                res = eval(expression)
                client.reply_message(f"🧮 *النتيجة:* `{res}`", message)
            except Exception:
                client.reply_message("❌ عملية حسابية غير صحيحة.", message)
        else:
            client.reply_message("⚠️ يُسمح بالأرقام والرموز (+ - * /) فقط.", message)
        return True

    return False
