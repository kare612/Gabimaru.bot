import logging
import threading
import time
from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv, PairStatusEv
from config import BOT_NAME, BOT_NUMBER, PREFIX
from plugins.general import handle_general_commands

logging.basicConfig(level=logging.INFO)

# إنشاء ملف الجلسة الخاص برقم البوت
client = NewClient("gabimaru.sqlite3")

def request_pairing_code():
    # الانتظار قليلاً لتهيئة الاتصال ثم طلب الكود للرقم 212784776925
    time.sleep(3)
    try:
        code = client.PairPhone(BOT_NUMBER, show_push_notification=True)
        print(f"\n==========================================")
        print(f"🔑 كود تفعيل البوت للرقم ({BOT_NUMBER}): {code}")
        print(f"==========================================\n")
    except Exception as e:
        print(f"⚠️ ملاحظة (قد يكون الرقم مرتبطاً بالفعل): {e}")

@client.event(ConnectedEv)
def on_connected(client: NewClient, event: ConnectedEv):
    print(f"\n✅ تم تشغيل {BOT_NAME} بنجاح على الرقم {BOT_NUMBER}!\n")

@client.event(PairStatusEv)
def on_pair_status(client: NewClient, event: PairStatusEv):
    print(f"🔗 تم الربط بنجاح مع الرقم: {event.ID.User}")

@client.event(MessageEv)
def on_message(client: NewClient, message: MessageEv):
    text = (
        message.Message.conversation
        or message.Message.extendedTextMessage.text
    )

    if not text:
        return

    text = text.strip()

    if text.startswith(PREFIX):
        handled = handle_general_commands(client, message, text)
        if not handled:
            client.reply_message(f"❌ أمر غير معروف. اكتب `{PREFIX}اوامر` لرؤية القائمة.", message)

if __name__ == "__main__":
    print(f"⏳ جاري تشغيل {BOT_NAME} وطلب كود التفعيل للرقم {BOT_NUMBER}...")
    # تشغيل دالة طلب الكود في الخلفية بالتوازي مع الاتصال
    threading.Thread(target=request_pairing_code, daemon=True).start()
    client.connect()
    
