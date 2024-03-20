import whisper
import os

def transcribe_audio(audio_file: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    os.remove(audio_file)
    return result['text']