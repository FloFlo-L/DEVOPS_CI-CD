from services.translation import translate_text

def test_translate_text_to_french():
    text = "Hello, how are you?"
    lang = "fr"
    result = translate_text(text, lang)
    assert result == "Bonjour, comment vas-tu?"
