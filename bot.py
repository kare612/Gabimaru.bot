import logging
from neonize.client import NewClient
from neonize.events import MessageEv, ConnectedEv, PairStatusEv
from config import BOT_NAME, BOT_NUMBER, ALLOWED_NUMBERS
from plugins.general import handle_general
from plugins.tools import handle_tools

# إخفاء السجلات الزائدة لكي يظهر كود الربط بوضوح تام
logging.basicConfig(level=logging.ERROR)

client = NewClient("gabimaru_session.sqlite3")

@client.event(PairStatusEv)
def on_pair_status(client: NewClient, event: PairStatusEv):
    print(f"\n🔗 حالة الاقتران: {event}\n")

@client.event(ConnectedEv)
def on_connected(client: NewClient, event: ConnectedEv):
    print(f"\n✅ تم ربط {BOT_NAME} بنجاح وهو يعمل الآن!\n")

@client.event(MessageEv)
def on_message(client: NewClient, message: MessageEv):
    try:
        text = (
            message.Message.conversation
            or message.Message.extendedTextMessage.text
            or ""
        ).strip()

        if not text:
            return

        sender = str(message.Info.MessageSource.Sender.User)
        is_from_me = message.Info.MessageSource.IsFromMe

        # يرد فقط على رقم المطور المحدد في config.py أو على رسائلك
        if not (is_from_me or any(num in sender for num in ALLOWED_NUMBERS)):
            return

        reply = handle_general(text) or handle_tools(text)
        if reply:
            client.reply_message(reply, message)

    except Exception as e:
        print(f"⚠️ خطأ: {e}")

if __name__ == "__main__":
    print("==========================================")
    print(f"⏳ جاري طلب كود الربط (8 أرقام/حروف) للرقم: +{BOT_NUMBER}")
    print("📱 افتح واتساب -> الأجهزة المرتبطة -> ربط جهاز -> الربط برقم الهاتف")
    print("==========================================\n")
    
    # هذه الدالة تطلب كود الاقتران مباشرة بدون إظهار QR Code
    client.PairPhone(BOT_NUMBER, show_push_notification=True)
    
