import os
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException, Body
from pytube import YouTube
from moviepy.editor import *
from google.cloud import translate_v2 as translate
import whisper
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

# Configuration initiale
api_key_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if not api_key_path:
    raise Exception('Le chemin de la clé API Google n\'est pas défini dans les variables d\'environnement.')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = api_key_path
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)

output_directory = "./videos"

app = FastAPI()

def translate_text(text, target_language):
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language=target_language)
    return translation['translatedText']

def download_video_with_timestamp(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{yt.title}_{timestamp}.mp4"
        output_file_path = f"{output_path}/{output_filename}"
        video.download(output_path, filename=output_filename)
        logging.info("Video downloaded successfully!")
        audio_file_path = f"{output_path}/{yt.title}_{timestamp}.mp3"
        video_clip = VideoFileClip(output_file_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file_path)
        audio_clip.close()
        video_clip.close()
        logging.info("Video converted to mp3 successfully!")
        return audio_file_path
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return None

def transcribe_audio(audio_file_path, model_path, target_language):
    model = whisper.load_model(model_path)
    result = model.transcribe(audio_file_path)
    translated_text = translate_text(result['text'], target_language)
    text_file_path = os.path.splitext(audio_file_path)[0] + ".txt"
    translated_text_file_path = os.path.splitext(audio_file_path)[0] + "_translated.txt"
    with open(text_file_path, "w") as text_file:
        text_file.write(result['text'])
    with open(translated_text_file_path, "w") as translated_text_file:
        translated_text_file.write(translated_text)
    logging.info(f"Transcript saved to: {text_file_path}")

# Endpoint FastAPI
@app.post("/process_video/")
async def process_video(video_url: str = Body(..., description="URL de la vidéo YouTube"), 
                        target_language: Optional[str] = Body("en", description="Langue cible pour la traduction")):
    try:
        audio_file_path = download_video_with_timestamp(video_url, output_directory)
        if audio_file_path:
            transcribe_audio(audio_file_path, "base", target_language)
            return {"message": "Traitement de la vidéo réussi"}
        else:
            raise HTTPException(status_code=500, detail="Échec du téléchargement de la vidéo")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))