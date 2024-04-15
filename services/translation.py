import deepl
from dotenv import load_dotenv
import os

# Charge les variables d'environnement du fichier .env
load_dotenv()

# Récupère la clé API de l'environnement
auth_key = os.getenv("API_DEEPL")
translator = deepl.Translator(auth_key)

def translate_text(text: str, lang: str) -> str:
    try:
        translation = translator.translate_text(text, target_lang=lang)
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
        raise
