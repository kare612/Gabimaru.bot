import sys
import json
from config import BOT_NAME, OWNER_NAME, OWNER_NUMBER, OWNER_LID, PREFIX
from plugins.general import handle_general
from plugins.tools import handle_tools
from plugins.dark_ai import handle_dark_ai
from plugins.islamic import handle_islamic

def main():
    if len(sys.argv) < 2:
        return

    try:
        raw_data = sys.argv.pop(1)
        data = json.loads(raw_data)
    except Exception:
        return

    text = data.get("text", "").strip()
    sender = data.get("sender", "")

    if not text.startswith(PREFIX):
        return

    is_owner = (OWNER_NUMBER in sender) or (OWNER_LID in sender)

    if text == f"{PREFIX}المطور":
        if is_owner:
            print(f"👑 أهلاً بك يا مطور البوت! لديك كامل الصلاحيات.")
        else:
            print(f"👑 مطور البوت هو: {OWNER_NAME}")
        return

    # تمرير الأمر على جميع أقسام البوت بالترتيب
    for handler in [handle_general, handle_tools, handle_dark_ai, handle_islamic]:
        reply = handler(text)
        if reply:
            print(reply)
            return

    print(f"❌ أمر غير معروف أو قيد التطوير. اكتب `{PREFIX}اوامر` لعرض القائمة.")

if __name__ == "__main__":
    main()
    
