import os
import logging
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pytube import YouTube
from moviepy.editor import *
from google.cloud import translate_v2 as translate
import whisper
from dotenv import load_dotenv  # Importez load_dotenv de python-dotenv

# Chargez les variables d'environnement du fichier .env
load_dotenv()

# Configuration initiale
api_key_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')  # Utilisez os.getenv pour accéder à la variable d'environnement
if not api_key_path:
    raise Exception('Le chemin de la clé API Google n\'est pas défini dans les variables d\'environnement.')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = api_key_path
logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO)

app = FastAPI()