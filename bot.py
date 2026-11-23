import sys
import json
from config import BOT_NAME, OWNER_NAME, OWNER_NUMBER, OWNER_LID, PREFIX
from plugins.general import handle_general
from plugins.tools import handle_tools

def main():
    if len(sys.argv) < 2:
        return

    try:
        raw_data = sys.argv.pop(1)
        data = json.loads(raw_data)
    except Exception as e:
        print(f"خطأ في قراءة البيانات: {e}")
        return

    text = data.get("text", "").strip()
    sender = data.get("sender", "")

    if not text.startswith(PREFIX):
        return

    # التحقق من صلاحية المطور عبر رقم الهاتف أو معرّف LID
    is_owner = (OWNER_NUMBER in sender) or (OWNER_LID in sender)

    if text == f"{PREFIX}المطور":
        if is_owner:
            print(f"👑 أهلاً بك يا مطور البوت ({OWNER_NAME})! لديك كامل الصلاحيات.")
        else:
            print(f"👑 مطور البوت هو: {OWNER_NAME}")
        return

    reply = handle_general(text)
    if reply:
        print(reply)
        return

    reply = handle_tools(text)
    if reply:
        print(reply)
        return

    print(f"❌ أمر غير معروف. اكتب `{PREFIX}اوامر` لعرض القائمة.")

if __name__ == "__main__":
    main()
    
