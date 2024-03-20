from googletrans import Translator

def translate_text(text: str, lang: str) -> str:
    translator = Translator()
    translated_text = translator.translate(text, dest=lang).text
    return translated_text
