from config import PREFIX

def handle_groups(text, is_group, quoted_sender):
    group_cmds = [
        f"{PREFIX}منشن", f"{PREFIX}مخفي", f"{PREFIX}قفل", f"{PREFIX}فتح",
        f"{PREFIX}رابط", f"{PREFIX}معلومات_المجموعة", f"{PREFIX}ترقية",
        f"{PREFIX}تخفيض", f"{PREFIX}طرد"
    ]

    # التحقق إذا كان الأمر يخص المجموعات
    base_cmd = text.split(" ").at(0) if " " in text else text
    if base_cmd not in group_cmds:
        return None

    if not is_group:
        return "⚠️ هذا الأمر يعمل داخل المجموعات فقط."

    if text == f"{PREFIX}قفل":
        return "GROUP_ACTION|close|🔒 تم قفل المجموعة (للمشرفين فقط)."
    elif text == f"{PREFIX}فتح":
        return "GROUP_ACTION|open|🔓 تم فتح المجموعة للجميع."
    elif text == f"{PREFIX}رابط":
        return "GROUP_ACTION|link|🔗 تفضل رابط المجموعة:"
    elif text == f"{PREFIX}معلومات_المجموعة":
        return "GROUP_ACTION|info|👥 معلومات المجموعة:"
    elif text.startswith(f"{PREFIX}منشن") or text.startswith(f"{PREFIX}مخفي"):
        msg_body = text.replace(f"{PREFIX}منشن", "").replace(f"{PREFIX}مخفي", "").strip()
        if not msg_body:
            msg_body = "🌑 تنبيه جماعي من بوت الظلام!"
        return f"GROUP_ACTION|tagall|{msg_body}"
    elif text.startswith(f"{PREFIX}ترقية"):
        if not quoted_sender:
            return "⚠️ رد على رسالة الشخص الذي تريد ترقيته لمشرف."
        return f"GROUP_ACTION|promote|{quoted_sender}"
    elif text.startswith(f"{PREFIX}تخفيض"):
        if not quoted_sender:
            return "⚠️ رد على رسالة المشرف الذي تريد تخفيضه."
        return f"GROUP_ACTION|demote|{quoted_sender}"
    elif text.startswith(f"{PREFIX}طرد"):
        if not quoted_sender:
            return "⚠️ رد على رسالة العضو الذي تريد طرده."
        return f"GROUP_ACTION|kick|{quoted_sender}"

    return None
      
