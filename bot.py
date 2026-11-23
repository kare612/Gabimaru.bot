import sys
import json
from config import BOT_NAME, OWNER_NAME, OWNER_NUMBER, OWNER_LID, PREFIX
from plugins.general import handle_general
from plugins.tools import handle_tools
from plugins.dark_ai import handle_dark_ai
from plugins.islamic import handle_islamic
from plugins.groups import handle_groups
from plugins.downloader import handle_downloader

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
    is_group = data.get("isGroup", False)
    quoted_sender = data.get("quotedSender", "")

    if not text.startswith(PREFIX):
        return

    is_owner = (OWNER_NUMBER in sender) or (OWNER_LID in sender)

    # أوامر المطور الخاصة
    if text == f"{PREFIX}المطور":
        if is_owner:
            print("👑 أهلاً بك يا مطور البوت! لديك كامل الصلاحيات.")
        else:
            print(f"👑 مطور البوت هو: {OWNER_NAME}")
        return

    if text in [f"{PREFIX}اعادة_تشغيل", f"{PREFIX}تحديث"] and is_owner:
        print("OWNER_ACTION|restart|🔄 جاري تحديث وسحب الملفات وإعادة تشغيل البوت...")
        return

    # فحص أوامر المجموعات
    group_reply = handle_groups(text, is_group, quoted_sender)
    if group_reply:
        print(group_reply)
        return

    # تمرير الأمر على باقي الأقسام
    for handler in [handle_general, handle_tools, handle_dark_ai, handle_islamic, handle_downloader]:
        reply = handler(text)
        if reply:
            print(reply)
            return

    print(f"❌ أمر غير معروف. اكتب `{PREFIX}اوامر` لعرض القائمة.")

if __name__ == "__main__":
    main()
    
