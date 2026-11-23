from config import PREFIX

def handle_group_commands(client, message, text):
    chat_jid = message.Info.MessageSource.Chat
    is_group = message.Info.MessageSource.IsGroup

    # التحقق أن الأمر يُستخدم داخل مجموعة
    if text in [f"{PREFIX}رابط", f"{PREFIX}link", f"{PREFIX}معلومات_المجموعة"]:
        if not is_group:
            client.reply_message("⚠️ هذا الأمر يعمل داخل المجموعات فقط.", message)
            return True

    # أمر جلب رابط دعوة المجموعة (يجب أن يكون البوت مشرفاً)
    if text in [f"{PREFIX}رابط", f"{PREFIX}link"]:
        try:
            link = client.get_group_invite_link(chat_jid)
            client.reply_message(f"🔗 *رابط المجموعة:*\n{link}", message)
        except Exception:
            client.reply_message("❌ فشل جلب الرابط. تأكد أن البوت مشرف (Admin) في المجموعة.", message)
        return True

    # أمر عرض معلومات المجموعة
    elif text == f"{PREFIX}معلومات_المجموعة":
        try:
            group_info = client.get_group_info(chat_jid)
            info_text = f"""
👥 *معلومات المجموعة:*
• *الاسم:* {group_info.GroupName.Name}
• *عدد الأعضاء:* {len(group_info.Participants)}
            """
            client.reply_message(info_text.strip(), message)
        except Exception as e:
            client.reply_message(f"❌ حدث خطأ أثناء جلب المعلومات.", message)
        return True

    return False
  
