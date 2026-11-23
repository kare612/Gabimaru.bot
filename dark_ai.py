import random
import urllib.request
import urllib.parse
from config import PREFIX

def handle_dark_ai(text):
    # 1. أمر الذكاء الاصطناعي (.ذكاء سؤالك)
    if text.startswith(f"{PREFIX}ذكاء ") or text.startswith(f"{PREFIX}اسال "):
        prompt = text.split(" ", 1)[1].strip()
        try:
            url = f"https://pollinations.ai{urllib.parse.quote(prompt)}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as res:
                answer = res.read().decode('utf-8').strip()
                return f"🔮 *رد الذكاء الاصطناعي:*\n\n{answer}"
        except Exception:
            return "⚠️ تعذر الاتصال بخادم الذكاء الاصطناعي حالياً، حاول بعد قليل."

    # 2. أمر الزخرفة (.زخرفة اسمك)
    elif text.startswith(f"{PREFIX}زخرفة "):
        word = text.replace(f"{PREFIX}زخرفة ", "").strip()
        styles = [
            f"꧁༒☬ {word} ☬༒꧂",
            f"★彡『 {word} 』彡★",
            f"🌑 ══•『 {word} 』•══ 🌑",
            f"♛ ╰• {word} •╯ ♛",
            f"么 {word} ズ",
            f"『✦』 {word} 『✦』"
        ]
        return "✨ *تفضل زخرفتك المزينة:*\n\n" + "\n".join(styles)

    # 3. أوامر الترفيه والظلام
    elif text == f"{PREFIX}لو_خيروك":
        options = [
            "لو خيروك بين العيش في الظلام الأبدي أو فقدان الذاكرة؟",
            "لو خيروك بين السفر عبر الزمن للماضي أو للمستقبل؟",
            "لو خيروك بين قراءة أفكار الناس أو الاختفاء عن الأنظار؟"
        ]
        return f"🗡️ *لو خيروك:*\n{random.choice(options)}"

    elif text == f"{PREFIX}صراحة":
        questions = [
            "ما هو أكبر سر تخفيه عن أقرب أصدقائك؟",
            "هل ندمت يوماً على قرار اتخذته في لحظة غضب؟",
            "من هو الشخص الذي لا تستطيع رفض طلب له؟"
        ]
        return f"🕯️ *سؤال صراحة:*\n{random.choice(questions)}"

    elif text == f"{PREFIX}تحدي":
        dares = [
            "أرسل آخر صورة التقطتها بهاتفك في المجموعة الآن!",
            "اكتب رسالة اعتراف مضحكة في الحالة (Status) لمدة 10 دقائق.",
            "أرسل إيموجي 💀 لآخر 3 أشخاص راسلوك."
        ]
        return f"🔥 *تحدي الظلام:*\n{random.choice(dares)}"

    elif text.startswith(f"{PREFIX}نسبة_الحب") or text.startswith(f"{PREFIX}نسبة_الذكاء") or text == f"{PREFIX}حظ":
        percent = random.randint(1, 100)
        return f"📊 *النتيجة هي:* `{percent}%` 🔮"

    return None
