import yt_dlp

video_url = 'https://www.youtube.com/watch?v=71DC6BnC6x8'

ydl_opts = {
    'outtmpl': 'test2.%(ext)s', # نام فایل خروجی برای ویدئو با پسوند ویدئو
    'format': 'best',           # دانلود بالاترین کیفیت
    'noplaylist': True,         # دانلود فقط ویدئو، نه لیست پخش
    'writesubtitles': True,     # دانلود زیرنویس‌ها
    'subtitleslangs': ['fa'],   # زبان زیرنویس‌ها (فارسی)
    'subtitlesformat': 'srt/vtt', # فرمت زیرنویس (در صورت موجود بودن)
    'writeautomaticsub': True,  # دانلود زیرنویس‌های خودکار (در صورت وجود)
    'outtmpl': {
    'default': 'video.%(ext)s',       # ذخیره ویدئو با نام ویدئو و پسوند آن
    'subtitles': 'subtitle.%(ext)s'   # ذخیره زیرنویس با نام subtitle و پسوند آن
    },
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print('دانلود ویدئو و زیرنویس‌ها به پایان رسید!')
except Exception as e:
    print(f'خطا در دانلود ویدئو و زیرنویس‌ها: {e}')