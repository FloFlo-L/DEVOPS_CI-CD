import pytest
from main import download_audio_from_youtube

def test_download_audio():
    # Test with a valid YouTube URL
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example URL
    audio_file = download_audio_from_youtube(url)
    assert audio_file.endswith(".mp4")  # Check if the file has been downloaded successfully

def test_download_audio_from_youtube_invalid_url():
    url = "invalid_url"  # Example invalid URL
    with pytest.raises(Exception):
        download_audio_from_youtube(url)

def test_download_audio_from_youtube_unavailable_video():
    # Test with a YouTube URL for an unavailable video
    url = "https://www.youtube.com/watch?v=non_existent_video"  # Example unavailable video URL
    with pytest.raises(Exception):
        download_audio_from_youtube(url)

def test_download_audio_from_youtube_no_audio_stream():
    # Test with a YouTube URL without an audio stream
    url = "https://www.youtube.com/watch?v=X1xwRRj3sJo"  # Example URL without audio stream
    with pytest.raises(Exception):
        download_audio_from_youtube(url)

def test_download_audio_from_youtube_empty_url():
    # Test with an empty YouTube URL
    url = ""
    with pytest.raises(Exception):
        download_audio_from_youtube(url)
