# test_translate_text.py

from main import translate_text

def test_translate_text():
    # Test de la fonction de traduction avec un texte donné
    text = "Ceci est un texte de test"
    target_language = "en"  # Langue cible (anglais)
    translated_text = translate_text(text, target_language)
    
    # Vérifier si la traduction est réussie
    assert translated_text is not None
    assert isinstance(translated_text, str)

    # Vous pouvez également ajouter d'autres assertions pour vérifier le contenu de la traduction, etc.
