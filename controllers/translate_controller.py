from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.youtube import download_audio_from_youtube
from services.transcription import transcribe_audio
from services.translation import translate_text
import os

router = APIRouter()

class TranslationRequest(BaseModel):
    url: str
    lang: str

@router.post("/translate")
async def translate_video(request_data: TranslationRequest):
    try:
        url = request_data.url
        lang = request_data.lang
        audio_file = download_audio_from_youtube(url)
        transcription = transcribe_audio(audio_file)
        os.remove(audio_file)
        translation = translate_text(transcription, lang)
        return {"translation": translation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
