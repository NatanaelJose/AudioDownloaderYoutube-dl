import youtube_dl
import os

# URL dos vídeos do YouTube
videos_urls = ['url do video', ' url do outro video']  # url dos videos

# Pasta de destino para download
output_path = './downloads/'


def download_audio(url):
    print("Downloading:", url)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Formato do áudio (MP3)
            'preferredquality': '192',  # Qualidade do áudio (192 kbps)
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        new_filename = os.path.splitext(filename)[0] + '.mp3'


for video_url in videos_urls:
    download_audio(video_url)
