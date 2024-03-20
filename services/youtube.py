from pytube import YouTube
import ssl

def download_audio_from_youtube(url: str) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(filename="temp_audio.mp4")
    return audio_file
