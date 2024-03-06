from fastapi import FastAPI, HTTPException
from pytube import YouTube
import whisper
import os
import ssl
from google.cloud import translate_v2 as translate

# Set the path to your API key JSON file
api_key = 'AIzaSyBserMzRBI--CPUQBg0hU5nVkIO81mwPFU'

app = FastAPI()

def download_audio_from_youtube(url: str) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context  # Désactiver la vérification SSL
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(filename="temp_audio")
    return audio_file

# Fonction pour transcrire l'audio en texte avec Whisper
def transcribe_audio(audio_file: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    os.remove(audio_file)  # Supprimer le fichier audio temporaire
    return result['text']  # Texte transcrit de l'audio

# Fonction pour traduire du texte dans une langue
def translate_text(text: str, lang: str) -> str:
    # Create an instance of the Translator class
    translate_client = translate.Client()
    # Use the translate() method to translate the text
    translation = translate_client.translate(text, target_language=lang)
    return translation['translatedText']

@app.post("/translate/")
async def translate_video(url: str, lang: str):
    try:
        # Télécharger l'audio de la vidéo YouTube
        audio_file = download_audio_from_youtube(url)
        # Transcrire l'audio en texte
        transcription = transcribe_audio(audio_file)
        # Traduire le texte dans une langue
        translation = translate_text(transcription, lang)
        return {
            "transcription": transcription,
            "translation": translation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))