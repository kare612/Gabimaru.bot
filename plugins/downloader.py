import urllib.request
import urllib.parse
import json
from config import PREFIX

def handle_downloader(text):
    # 1. البحث عن صور أو خلفيات (.صورة قطط / .خلفية انمي)
    if text.startswith(f"{PREFIX}صورة ") or text.startswith(f"{PREFIX}خلفية "):
        query = text.split(" ", 1).at(1).strip()
        encoded = urllib.parse.quote(query)
        image_url = f"https://pollinations.ai{encoded}"
        return f"IMAGE|{image_url}|🖼️ *نتيجة البحث عن:* {query}"

    # 2. الطقس (.طقس الناظور)
    elif text.startswith(f"{PREFIX}طقس "):
        city = text.replace(f"{PREFIX}طقس ", "").strip()
        try:
            url = f"https://wttr.in{urllib.parse.quote(city)}?format=%C+%t+%w&lang=ar"
            req = urllib.request.Request(url, headers={'User-Agent': 'curl/7.68.0'})
            with urllib.request.urlopen(req, timeout=10) as res:
                weather = res.read().decode('utf-8').strip()
                return f"🌤️ *حالة الطقس في {city}:*\n{weather}"
        except Exception:
            return "⚠️ تعذر جلب حالة الطقس لهذه المدينة."

    # 3. تحميل يوتيوب / صوت / فيديو عبر yt-dlp في بايثون
    elif text.startswith(f"{PREFIX}يوتيوب ") or text.startswith(f"{PREFIX}اغنية ") or text.startswith(f"{PREFIX}صوت "):
        query = text.split(" ", 1).at(1).strip()
        return f"DOWNLOAD_AUDIO|{query}"

    elif text.startswith(f"{PREFIX}فيديو ") or text.startswith(f"{PREFIX}تيك_توك "):
        query = text.split(" ", 1).at(1).strip()
        return f"DOWNLOAD_VIDEO|{query}"

    return None
  
