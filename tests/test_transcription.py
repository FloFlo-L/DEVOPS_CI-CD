from services.transcription import transcribe_audio

def test_transcribe_audio():
    result = transcribe_audio('test_audio.mp3')
    assert isinstance(result, str)
    assert len(result) > 0