from config import BOT_NAME, OWNER_NAME, PREFIX

MENU_IMAGE = "https://ibb.co/pjc1FPp4"

def handle_general(text):
    if text == f"{PREFIX}ping":
        return "⚡ *سُـرعـة الـظـلام:* البوت يعمل بأقصى طاقة (Python 🐍)!"
    
    elif text in [f"{PREFIX}menu", f"{PREFIX}اوامر"]:
        dark_menu = f"""🌑 ═══ •『 𝐆𝐀𝐁𝐈𝐌𝐀𝐑𝐔 𝐃𝐀𝐑𝐊 』• ═══ 🌑
👑 *الـمـطـور:* {OWNER_NAME}
⚔️ *الـبـادئـة:* ( {PREFIX} )
📊 *إجـمـالـي الأوامـر:* 233 أمـر مُـفـعّـل

╔═══ ❖ •『 قـسـم الـمـطـور 』• ❖ ═══╗
🕯️ {PREFIX}المطور
🕯️ {PREFIX}تفعيل
🕯️ {PREFIX}تعطيل
🕯️ {PREFIX}اذاعة
🕯️ {PREFIX}حظر
🕯️ {PREFIX}فك_حظر
🕯️ {PREFIX}اعادة_تشغيل
🕯️ {PREFIX}ايقاف
🕯️ {PREFIX}تحديث
🕯️ {PREFIX}سجل
🕯️ {PREFIX}نسخة
🕯️ {PREFIX}وضع_خاص
🕯️ {PREFIX}وضع_عام
🕯️ {PREFIX}تغيير_الاسم
🕯️ {PREFIX}تغيير_الصورة
🕯️ {PREFIX}المتصلين
🕯️ {PREFIX}المجموعات
🕯️ {PREFIX}مغادرة
🕯️ {PREFIX}انضمام
🕯️ {PREFIX}صلاحيات

╔═══ ❖ •『 قـسـم الـمـجـمـوعـات 』• ❖ ═══╗
🖤 {PREFIX}رابط
🖤 {PREFIX}تغيير_الرابط
🖤 {PREFIX}معلومات_المجموعة
🖤 {PREFIX}منشن
🖤 {PREFIX}مخفي
🖤 {PREFIX}طرد
🖤 {PREFIX}اضافة
🖤 {PREFIX}ترقية
🖤 {PREFIX}تخفيض
🖤 {PREFIX}قفل
🖤 {PREFIX}فتح
🖤 {PREFIX}تغيير_الوصف
🖤 {PREFIX}تغيير_الاسم_جروب
🖤 {PREFIX}تحذير
🖤 {PREFIX}حذف_تحذير
🖤 {PREFIX}التحذيرات
🖤 {PREFIX}مضاد_روابط
🖤 {PREFIX}مضاد_سبام
🖤 {PREFIX}ترحيب
🖤 {PREFIX}وداع
🖤 {PREFIX}قوانين
🖤 {PREFIX}المشرفين
🖤 {PREFIX}الاعضاء
🖤 {PREFIX}حذف
🖤 {PREFIX}تثبيت

╔═══ ❖ •『 قـسـم الـتـحـمـيـل 』• ❖ ═══╗
🕷️ {PREFIX}يوتيوب
🕷️ {PREFIX}فيديو
🕷️ {PREFIX}صوت
🕷️ {PREFIX}تيك_توك
🕷️ {PREFIX}انستا
🕷️ {PREFIX}فيسبوك
🕷️ {PREFIX}تويتر
🕷️ {PREFIX}تطبيق
🕷️ {PREFIX}صورة
🕷️ {PREFIX}خلفية
🕷️ {PREFIX}انمي
🕷️ {PREFIX}مانجا
🕷️ {PREFIX}حلقة
🕷️ {PREFIX}اغنية
🕷️ {PREFIX}كلمات
🕷️ {PREFIX}بحث
🕷️ {PREFIX}رابط_مباشر
🕷️ {PREFIX}ضغط
🕷️ {PREFIX}ملف
🕷️ {PREFIX}تورنت

╔═══ ❖ •『 الـذكـاء والـتـحـويـل 』• ❖ ═══╗
🔮 {PREFIX}ذكاء
🔮 {PREFIX}اسال
🔮 {PREFIX}تخيل
🔮 {PREFIX}رسم
🔮 {PREFIX}ملصق
🔮 {PREFIX}سرقة
🔮 {PREFIX}لصورة
🔮 {PREFIX}لفيديو
🔮 {PREFIX}لصوت
🔮 {PREFIX}ترجمة
🔮 {PREFIX}زخرفة
🔮 {PREFIX}نطق
🔮 {PREFIX}باركود
🔮 {PREFIX}قراءة_باركود
🔮 {PREFIX}اختصار
🔮 {PREFIX}طقس
🔮 {PREFIX}عملة
🔮 {PREFIX}تاريخ
🔮 {PREFIX}وقت
🔮 {PREFIX}احسب

╔═══ ❖ •『 قـسـم الـظـلام والـتـرفـيـه 』• ❖ ═══╗
🗡️ {PREFIX}حكمة
🗡️ {PREFIX}اقتباس
🗡️ {PREFIX}شعر
🗡️ {PREFIX}قصة
🗡️ {PREFIX}لغز
🗡️ {PREFIX}سؤال
🗡️ {PREFIX}تحدي
🗡️ {PREFIX}صراحة
🗡️ {PREFIX}جراة
🗡️ {PREFIX}العب
🗡️ {PREFIX}اكس_او
🗡️ {PREFIX}حجر
🗡️ {PREFIX}نرد
🗡️ {PREFIX}حظ
🗡️ {PREFIX}نسبة_الحب
🗡️ {PREFIX}نسبة_الذكاء
🗡️ {PREFIX}شخصية
🗡️ {PREFIX}لو_خيروك
🗡️ {PREFIX}كت
🗡️ {PREFIX}تويت
🗡️ {PREFIX}فزورة
🗡️ {PREFIX}معلومة
🗡️ {PREFIX}هل_تعلم
🗡️ {PREFIX}نكتة
🗡️ {PREFIX}تقييم
🗡️ {PREFIX}بصمة
🗡️ {PREFIX}كشف
🗡️ {PREFIX}توقعات
🗡️ {PREFIX}ابراج
🗡️ {PREFIX}رمزية

╔═══ ❖ •『 قـسـم الإسـلامـيـات 』• ❖ ═══╗
🌙 {PREFIX}قران
🌙 {PREFIX}اية
🌙 {PREFIX}سورة
🌙 {PREFIX}حديث
🌙 {PREFIX}اذكار
🌙 {PREFIX}صباح
🌙 {PREFIX}مساء
🌙 {PREFIX}دعاء
🌙 {PREFIX}تفسير
🌙 {PREFIX}اسماء_الله
🌙 {PREFIX}مواقيت
🌙 {PREFIX}قصة_نبي
🌙 {PREFIX}صحابي
🌙 {PREFIX}فتوى
🌙 {PREFIX}تسبيح

🌑 ═══ •『 𝐆𝐀𝐁𝐈𝐌𝐀𝐑𝐔 𝐁𝐎𝐓 』• ═══ 🌑"""
        return f"IMAGE|{MENU_IMAGE}|{dark_menu}"

    elif text == f"{PREFIX}info":
        return f"⚔️ *{BOT_NAME}*\nيعمل بلغة Python 🐍 تحت إشراف المطور {OWNER_NAME}."

    return None
