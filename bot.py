import logging
import threading
import time
from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv, PairStatusEv
from neonize.proto.waCompanionReg.WACompanionReg_pb2 import DeviceProps
from config import BOT_NAME, BOT_NUMBER, PREFIX

from plugins.general import handle_general_commands
from plugins.owner import handle_owner_commands
from plugins.group import handle_group_commands
from plugins.tools import handle_tools_commands

logging.basicConfig(level=logging.INFO)

# فرض رقم إصدار واتساب حديث لتجاوز خطأ Client outdated (405)
version_props = DeviceProps(
    os="Ubuntu",
    platformType=DeviceProps.DESKTOP,
    version=DeviceProps.AppVersion(primary=2, secondary=3000, tertiary=1058942110)
)

client = NewClient("gabimaru.sqlite3", props=version_props)

def request_pairing_code():
    time.sleep(4)
    try:
        code = client.PairPhone(BOT_NUMBER, show_push_notification=True)
        print(f"\n==========================================")
        print(f"🔑 كود تفعيل البوت للرقم ({BOT_NUMBER}): {code}")
        print(f"==========================================\n")
    except Exception as e:
        print(f"⚠️ ملاحظة الجلسة: {e}")

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
    sender = message.Info.MessageSource.Sender.User

    if text.startswith(PREFIX):
        if handle_general_commands(client, message, text): return
        if handle_owner_commands(client, message, text, sender): return
        if handle_group_commands(client, message, text): return
        if handle_tools_commands(client, message, text): return
        client.reply_message(f"❌ أمر غير معروف. اكتب `{PREFIX}اوامر` لعرض القائمة.", message)

if __name__ == "__main__":
    print(f"⏳ جاري تشغيل {BOT_NAME} وطلب كود التفعيل للرقم {BOT_NUMBER}...")
    threading.Thread(target=request_pairing_code, daemon=True).start()
    client.connect()
            
