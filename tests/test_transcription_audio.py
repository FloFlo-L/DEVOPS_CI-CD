import os
import pytest
from services.transcription import transcribe_audio

@pytest.fixture
def mock_whisper_load_model(mocker):
    return mocker.patch('services.transcription.whisper.load_model')

def test_transcribe_audio_valid(mock_whisper_load_model, tmp_path):
    mock_whisper_load_model.return_value.transcribe.return_value = {'text': 'Transcription réussie'}

    temp_audio_path = tmp_path / "valid_audio.mp4"
    temp_audio_path.touch()

    result = transcribe_audio(str(temp_audio_path))

    assert result == 'Transcription réussie'

def test_transcribe_audio_invalid(mock_whisper_load_model, tmp_path):
    mock_whisper_load_model.return_value.transcribe.side_effect = Exception("Erreur lors de la transcription")

    temp_audio_path = tmp_path / "invalid_audio.mp4"
    temp_audio_path.touch()

    with pytest.raises(Exception) as exc_info:
        transcribe_audio(str(temp_audio_path))

    assert str(exc_info.value) == "Erreur lors de la transcription"
