from translate import Translator

def translate_text(text: str, lang: str) -> str:
    translator = Translator(to_lang=lang)
    return translator.translate(text)
