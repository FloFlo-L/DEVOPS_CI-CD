import pytest
from services.translation import translate_text

def test_translate_text(mocker):
    # Créer un mock pour la méthode translate du Translator
    mock_translate = mocker.patch('googletrans.Translator.translate', autospec=True)
    
    # Définir la valeur de retour du mock pour simuler une traduction
    mock_translate.return_value.text = "Hola, ¿cómo estás?"

    # Test avec un texte et une langue valides
    text = "Hello, how are you?"
    lang = "es"
    translated_text = translate_text(text, lang)
    assert translated_text == "Hola, ¿cómo estás?"

def test_translate_text_invalid_lang():
    # Test avec une langue invalide
    text = "Hello, how are you?"
    lang = "invalid_lang"
    with pytest.raises(Exception):
        translate_text(text, lang)

def test_translate_text_empty_text():
    
    # Test avec un texte vide
    text = ""
    lang = "es"
    with pytest.raises(Exception):
        translate_text(text, lang)