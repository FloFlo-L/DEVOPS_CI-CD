from unittest import mock
from main import translate_text 

@mock.patch('main.translate.Client')
def test_translate_text(mock_client):
    # Configurez le mock pour retourner une réponse simulée
    mock_translate = mock_client.return_value.translate
    mock_translate.return_value = {'translatedText': 'Texte traduit'}

    # Appel de la fonction translate_text avec des données de test
    result = translate_text("Texte original", "fr")

    # Vérification que la fonction retourne le texte traduit attendu
    assert result == 'Texte traduit'

    # Vérification que le mock a été appelé comme prévu
    mock_translate.assert_called_once_with("Texte original", target_language="fr")
