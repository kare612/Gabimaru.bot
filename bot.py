import sys
import json
from config import BOT_NAME, OWNER_NAME, OWNER_NUMBER, PREFIX
from plugins.general import handle_general
from plugins.tools import handle_tools

def main():
    if len(sys.argv) < 2:
        return

    data = json.loads(sys.argv[1])
    text = data.get("text", "").strip()
    sender = data.get("sender", "")

    if not text.startswith(PREFIX):
        return

    # 1. التحقق من أوامر المطور
    if text == f"{PREFIX}المطور":
        if OWNER_NUMBER in sender:
            print(f"👑 أهلاً بك يا مطور البوت ({OWNER_NAME})! لديك كامل الصلاحيات.")
        else:
            print(f"👑 مطور البوت هو: {OWNER_NAME}")
        return

    # 2. تمرير الأمر إلى ملف الأوامر العامة (Python)
    reply = handle_general(text)
    if reply:
        print(reply)
        return

    # 3. تمرير الأمر إلى ملف الأدوات والألعاب (Python)
    reply = handle_tools(text)
    if reply:
        print(reply)
        return

    print(f"❌ أمر غير معروف. اكتب `{PREFIX}اوامر` لعرض القائمة.")

if __name__ == "__main__":
    main()
  
