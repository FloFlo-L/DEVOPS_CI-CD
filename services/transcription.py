import whisper

def transcribe_audio(audio_file: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, fp16=False)
    return result['text']
