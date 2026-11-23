import random
from config import PREFIX

def deco_text(s):
    m = {
        'ا':'آ','ب':'بٰـ','ت':'تـ','ث':'ثـ','ج':'جـ','ح':'حـ','خ':'خـ',
        'د':'دِ','ذ':'ذِ','ر':'رٰ','ز':'زٰ','س':'سـ','ش':'شـ','ص':'صـ',
        'ض':'ضـ','ط':'طـ','ظ':'ظـ','ع':'عـ','غ':'غـ','ف':'فـ','ق':'قـ',
        'ك':'كـ','ل':'لـ','م':'مـ','ن':'نـ','ه':'هـ','و':'وٰ','ي':'يـ'
    }
    return '『 ' + ''.join(m.get(c, c) for c in s) + ' 』'

def handle_tools(text):
    cmd = text.lower()

    if cmd == f"{PREFIX}حكمة":
        quotes = [
            "«القوة الحقيقية في السيطرة على نفسك.» - غابيمارو 🔥",
            "«الضعفاء يبحثون عن الأعذار، والأقوياء يصنعون الطرق.» - جين وو ⚔️",
            "«الألم يجعلك أقوى، والخوف يجعلك أشجع.» 🖤"
        ]
        return f"📜 *حكمة اليوم:*\n{random.choice(quotes)}"

    elif cmd == f"{PREFIX}ذكر":
        adhkar = [
            "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ ، سُبْحَانَ اللَّهِ الْعَظِيمِ 🌿",
            "اللَّهُمَّ صَلِّ وَسَلِّمْ وَبَارِكْ عَلَى نَبِيِّنَا مُحَمَّدٍ ﷺ ✨",
            "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ وَأَتُوبُ إِلَيْهِ 🤍"
        ]
        return random.choice(adhkar)
    
    elif cmd.startswith(f"{PREFIX}احسب "):
        try:
            expr = text[len(f"{PREFIX}احسب "):].strip()
            allowed = set("0123456789+-*/(). ")
            if all(c in allowed for c in expr) and expr:
                return f"🧮 *النتيجة:* {eval(expr)}"
            return "❌ يرجى إدخال أرقام وعمليات حسابية صحيحة فقط."
        except Exception:
            return "❌ خطأ في العملية الحسابية."

    elif cmd == f"{PREFIX}العب":
        choices = ["حجر 🪨", "ورقة 📄", "مقص ✂️"]
        return f"🎮 *اختياري هو:* {random.choice(choices)}"

    elif cmd.startswith(f"{PREFIX}زخرفة "):
        word = text[len(f"{PREFIX}زخرفة "):].strip()
        if not word:
            return f"⚠️ اكتب الكلمة بعد الأمر. مثال: `{PREFIX}زخرفة غابيمارو`"
        return deco_text(word)

    return None
  
