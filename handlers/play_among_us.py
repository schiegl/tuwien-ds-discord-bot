from intent import Intent, IntentName
from typing import Optional
import discord
import random

from handlers.handler import MessageHandler


class PlayAmongUs(MessageHandler):
    """
    Respond cheeky messages to people who want to play Among Us
    """

    def __init__(self):
        super().__init__(channels=["among-us"], intent_names=[IntentName.play_among_us])

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        if intent.probability > 0.9:
            return random.choice(
                [
                    f"{message.author.display_name} sus",
                    "Seems like the perfect time to play among us",
                    "Tell me more 🤔",
                    "I wish I could 😞",
                ]
            )
        else:
            return None

