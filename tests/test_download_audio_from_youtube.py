import pytest
import os
from main import download_audio_from_youtube

def test_download_audio():
    # Test with a valid YouTube URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    audio_file = download_audio_from_youtube(url)
    assert audio_file.endswith(".mp4")  # Check if the file has been downloaded successfully
    os.remove(audio_file)

def test_download_audio_from_youtube_invalid_url():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXc"  # Example invalid URL
    with pytest.raises(Exception):
        download_audio_from_youtube(url)

