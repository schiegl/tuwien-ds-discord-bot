from typing import Dict, Optional
import discord
from datetime import datetime, timedelta

from handlers.handler import MessageHandler
from intent import Intent, IntentName
from tests.utils import create_message


class EchoHandler(MessageHandler):
    def __init__(self, channels=[], intents=[], timeout=0):
        super().__init__(channels=channels, intent_names=intents, timeout=timeout)

    def handle(self, message: discord.Message, intent: Dict) -> Optional[str]:
        return message.content


def test_ignore_other_channels():
    handler = EchoHandler(channels=["a"])

    message = create_message("hello", channel="a")
    response = handler(message, None)
    assert response == "hello"

    message = create_message("hello", channel="b")
    response = handler(message, None)
    assert response is None


def test_respond_to_all_channels():
    handler = EchoHandler()

    for channel in ["a", "b", "c", "d"]:
        message = create_message("hello", channel=channel)
        response = handler(message, None)
        assert response == "hello"


def test_ignore_other_intents():
    handler = EchoHandler(intents=[IntentName.tell_wise_quote, IntentName.play_among_us])

    message = create_message("hello", channel="a")
    assert handler(message, Intent(name=IntentName.tell_wise_quote, probability=0.9)) == "hello"

    message = create_message("hello", channel="a")
    assert handler(message, Intent(name=IntentName.play_among_us, probability=0.9)) == "hello"

    message = create_message("hello", channel="a")
    assert handler(message, Intent(name=IntentName.thank_bot, probability=0.9)) is None


def test_response_timeout():
    handler = EchoHandler(timeout=10)

    now = datetime.now() - timedelta(seconds=11)

    message = create_message("hello", channel="a", created_at=now)
    response = handler(message, None)
    assert response == "hello"

    message = create_message("hello", channel="a", created_at=now + timedelta(seconds=9))
    response = handler(message, None)
    assert response is None

    message = create_message("hello", channel="a", created_at=now + timedelta(seconds=11))
    response = handler(message, None)
    assert response == "hello"
