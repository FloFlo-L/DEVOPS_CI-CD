from fastapi import APIRouter, HTTPException
from services.youtube import download_audio_from_youtube
from services.translation import translate_text
from services.transcription import transcribe_audio

router = APIRouter()

@router.post("/translate/")
async def translate_video(url: str, lang: str):
    try:
        audio_file = download_audio_from_youtube(url)
        transcription = transcribe_audio(audio_file)
        translation = translate_text(transcription, lang)
        return {"translation": translation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
