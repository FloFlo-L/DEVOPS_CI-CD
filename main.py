from fastapi import FastAPI, HTTPException
from pytube import YouTube
import whisper
import os
import ssl
from googletrans import Translator

app = FastAPI()

def download_audio_from_youtube(url: str) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context  # Désactiver la vérification SSL
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(filename="temp_audio.mp4")
    return audio_file

# Fonction pour transcrire l'audio en texte avec Whisper
def transcribe_audio(audio_file: str) -> str:
    model = whisper.load_model("base")  # Charger le modèle sans spécifier l'argument force_fp32
    result = model.transcribe(audio_file)
    os.remove(audio_file)  # Supprimer le fichier audio temporaire
    return result['text']  # Texte transcrit de l'audio

# Fonction pour traduire le texte
def translate_text(text: str, target_language: str = 'en') -> str:
    # Initialiser le traducteur
    translator = Translator()
    # Traduire le texte dans la langue cible
    translated_text = translator.translate(text, dest=target_language).text
    
    return translated_text

@app.post("/translate/")
async def translate_video(url: str):
    try:
        # Télécharger l'audio de la vidéo YouTube
        audio_file = download_audio_from_youtube(url)
        # Transcrire l'audio en texte
        transcription = transcribe_audio(audio_file)
        return {"transcription": transcription}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
