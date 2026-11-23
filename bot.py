import logging
import os
import threading
import time
import neonize
from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv, PairStatusEv
from config import BOT_NAME, BOT_NUMBER, PREFIX

from plugins.general import handle_general_commands
from plugins.owner import handle_owner_commands
from plugins.group import handle_group_commands
from plugins.tools import handle_tools_commands

logging.basicConfig(level=logging.INFO)

# --- دالة الإصلاح التلقائي لخطأ Client Outdated (405) ---
def auto_patch_neonize():
    old_ver = b"1042386815"
    new_ver = b"1068942110" # إصدار واتساب حديث بنفس عدد الخانات
    patched = False

    # البحث في مسار المكتبة ومسار التخزين المؤقت في Termux
    search_paths = [
        os.path.dirname(neonize.__file__),
        os.path.expanduser("~/.cache"),
        os.getcwd()
    ]

    for base_path in search_paths:
        if not os.path.exists(base_path):
            continue
        for root, _, files in os.walk(base_path):
            for file in files:
                if file.endswith(".so"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            data = f.read()
                        if old_ver in data:
                            with open(file_path, "wb") as f:
                                f.write(data.replace(old_ver, new_ver))
                            patched = True
                    except Exception:
                        pass
    if patched:
        print("🛠️ تم تحديث بروتوكول واتساب تلقائياً لتجاوز خطأ 405!")

# تنفيذ الإصلاح التلقائي قبل تشغيل البوت
auto_patch_neonize()
# ---------------------------------------------------------

client = NewClient("gabimaru.sqlite3")

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
