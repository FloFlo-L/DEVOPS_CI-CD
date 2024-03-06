import os
import pytest
from main import transcribe_audio

@pytest.fixture
def audio_file_path_invalid():
    # Créez un fichier audio temporaire invalide pour les tests
    temp_audio_path = "invalid_audio.mp4"
    with open(temp_audio_path, "w") as f:
        f.write("Contenu audio invalide")
    yield temp_audio_path
    # Supprimez le fichier audio temporaire après les tests
    os.remove(temp_audio_path)

@pytest.fixture
def audio_file_path_valid(tmp_path):
    # Créez un fichier audio temporaire valide pour les tests
    temp_audio_path = tmp_path / "valid_audio.mp4"
    temp_audio_path.touch()  # Créez un fichier audio temporaire vide
    yield temp_audio_path
    # Supprimez le fichier audio temporaire après les tests
    temp_audio_path.unlink()

@pytest.mark.filterwarnings("ignore::UserWarning")  # Ignorer tous les avertissements de type UserWarning
def test_transcribe_audio_empty_file():
    # Testez la fonction transcribe_audio avec un fichier audio vide
    temp_audio_path = "empty_audio.mp4"
    open(temp_audio_path, "w").close()  # Créez un fichier audio vide
    with pytest.raises(Exception):
        transcribe_audio(temp_audio_path)

@pytest.mark.filterwarnings("ignore::UserWarning")  # Ignorer tous les avertissements de type UserWarning
def test_transcribe_audio_unsupported_file(audio_file_path_valid):
    # Testez la fonction transcribe_audio avec un fichier audio valide mais non pris en charge
    with pytest.raises(Exception):
        transcribe_audio(audio_file_path_valid)