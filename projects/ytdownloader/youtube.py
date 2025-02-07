import sys
from pytubefix import YouTube

# Ensure a URL is provided
if len(sys.argv) < 2:
    print("Usage: python youtube.py <YouTube-URL>")
    sys.exit(1)

link = sys.argv[1]

try:
    yt = YouTube(link)
    yd = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    print(f"title: {yt.title} description: {yt.description}")
    yd.download(r"projects\ytdownloader\downloads")
except Exception as e:
    print(f"Error: {e}")


# import yt_dlp
# import sys


# url = sys.argv[1]
# ydl_opts = {
#         'format': 'bv*[ext=mp4]+ba[ext=m4a]',
#         'outtmpl': r"E:\Programming\Google  Python\Python-Phase\projects\ytdownloader\downloads\%(title)s.%(ext)s"
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(url, download=True)
#     print(f"Title: {info.get('title', 'Unknown')}")
#     print(f"Description: {info.get('description', 'No description')}")
#     ydl.download([url])
