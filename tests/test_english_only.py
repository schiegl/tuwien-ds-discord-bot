import pytest

from handlers.english_only import EnglishOnly
from tests.utils import create_message


@pytest.fixture
def handler():
    return EnglishOnly()


def test_only_german(handler):
    response = handler.handle(create_message("Wer hat die Aufgabe 3 gelöst?"), intent={})
    assert response is not None


def test_german_with_some_english(handler):
    response = handler.handle(create_message("Wer ist bei Among Us dabei?"), intent={})
    assert response is not None


def test_only_english(handler):
    response = handler.handle(create_message("Who solved task 3?"), intent={})
    assert response is None


def test_really_short_message(handler):
    response = handler.handle(create_message("I got 3"), intent={})
    assert response is None
