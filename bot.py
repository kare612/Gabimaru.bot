import logging
from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv
from neonize.utils import log

log.setLevel(logging.INFO)

# إنشاء جلسة البوت باسم غبيمارو
client = NewClient("gabimaru_session.sqlite3")

@client.event(ConnectedEv)
def on_connected(client: NewClient, _: ConnectedEv):
    print("✅ تم ربط بوت غبيمارو بنجاح وهو الآن قيد التشغيل!")

@client.event(MessageEv)
def on_message(client: NewClient, message: MessageEv):
    # استخراج نص الرسالة
    text = message.Message.conversation or message.Message.extendedTextMessage.text
    if not text:
        return

    chat = message.Info.MessageSource.Chat
    cmd = text.strip().lower()

    # 1. أمر فحص البوت
    if cmd == ".تست":
        client.reply_message("🔥 بوت غبيمارو شغال بنجاح!", message)

    # 2. قائمة أوامر غبيمارو
    elif cmd == ".اوامر" or cmd == ".الاوامر":
        menu = (
            "⚔️ *قائمة أوامر بوت غبيمارو* ⚔️\n\n"
            "🔹 *.تست* : فحص سرعة واستجابة البوت\n"
            "🔹 *.معلومات* : عرض معلومات البوت والمطور\n"
            "🔹 *.المطور* : التواصل مع مالك البوت\n\n"
            "⚡ *الحالة:* متصل (Termux Python)"
        )
        client.reply_message(menu, message)

    # 3. أمر المعلومات
    elif cmd == ".معلومات":
        info = (
            "🤖 *اسم البوت:* Gabimaru Bot\n"
            "💻 *النظام:* Python on Termux\n"
            "👤 *المالك:* kare612"
        )
        client.reply_message(info, message)

    # 4. أمر المطور
    elif cmd == ".المطور":
        client.reply_message("👑 حساب المطور: ://github.com", message)

# تشغيل البوت
client.connect()
  
