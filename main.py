import youtube_dl
import os

# URL do vídeo do YouTube
video_url = 'https://youtu.be/MURua52_YPg'

# Pasta de destino para download
output_path = './downloads/'


def download_audio(url):
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
        os.rename(filename, new_filename)


download_audio(video_url)
