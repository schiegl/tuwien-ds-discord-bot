from intent import Intent
from typing import Optional
import discord
from langdetect import detect
import random

from handlers.handler import MessageHandler


class EnglishOnly(MessageHandler):
    """
    If message has 4 or more words and is german this handler will respond with a reminder to keep the chat English.
    """

    def __init__(self):
        # wait 10 minutes before running handler again
        super().__init__(timeout=10 * 60)

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        text = message.content
        if len(text.split(" ")) >= 4 and detect(message.content) == "de":
            return random.choice(
                [
                    "Please keep the chat English 🙏",
                    "English please 🙏",
                    "Don't forget that not everyone speaks German on this server!",
                    "> Wish I'd speak German 🥺\n>  - *probably someone on this server*",
                ]
            )
        else:
            return None

