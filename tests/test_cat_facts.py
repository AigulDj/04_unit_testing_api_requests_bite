from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_cat_facts():
    mock_requester = Mock()
    mock_response = Mock()

    mock_requester.get.return_value = mock_response
    mock_response.json.return_value = {
        "fact": "Cats with long, lean bodies are more likely to be outgoing, and more protective and vocal than those with a stocky build."
    }

    cat_facts = CatFacts(mock_requester)
    assert cat_facts.provide() == "Cat fact: Cats with long, lean bodies are more likely to be outgoing, and more protective and vocal than those with a stocky build."
