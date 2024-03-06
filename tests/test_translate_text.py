from main import translate_text

def test_translate_text():
    # Test de la fonction de traduction avec un texte donné
    text = "Ceci est un texte de test"
    target_language = "en"  # Langue cible (anglais)
    translated_text = translate_text(text, target_language)