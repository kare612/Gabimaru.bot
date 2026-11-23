import sys
import os
from config import OWNER_NUMBER, PREFIX

def handle_owner_commands(client, message, text, sender):
    # التحقق أن المرسل هو رقم المطور
    if OWNER_NUMBER not in sender:
        return False

    # أمر إعادة تشغيل البوت
    if text == f"{PREFIX}restart" or text == f"{PREFIX}اعادة_تشغيل":
        client.reply_message("🔄 جاري إعادة تشغيل البوت...", message)
        os.execl(sys.executable, sys.executable, *sys.argv)
        return True

    # أمر إيقاف البوت نهائياً
    elif text == f"{PREFIX}stop" or text == f"{PREFIX}ايقاف":
        client.reply_message("🛑 تم إيقاف البوت من طرف المطور.", message)
        sys.exit(0)
        return True

    # أمر فحص صلاحية المطور
    elif text == f"{PREFIX}المطور":
        client.reply_message("👑 أهلاً بك يا مطور البوت! لديك كامل الصلاحيات.", message)
        return True

    return False
  
