# test_main.py
import pytest
from main import translate_text

@pytest.mark.parametrize("input_text, target_lang, expected", [
    ("Bonjour", "en", "Hello"),
    ("Hello", "fr", "Bonjour"),
])

def test_translate_text(input_text, target_lang, expected, mocker):
    mock_translate = mocker.patch('googletrans.Translator.translate')
    mock_translate.return_value = type('Translate', (object,), {'text': expected})()

    result = translate_text(input_text, target_lang)
    assert result == expected
    mock_translate.assert_called_once()
