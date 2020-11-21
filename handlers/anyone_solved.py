from intent import Intent, IntentName
from typing import Optional
import discord
import random

from handlers.handler import MessageHandler


class AnyoneSolved(MessageHandler):
    """
    Respond cheeky messages to people asking if someone else solved exercise
    """

    def __init__(self):
        super().__init__(intent_names=[IntentName.anyone_solved])

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        if intent.probability > 0.9:
            return random.sample([
                "Yes, I wish could tell you...",
                "Probably",
                "Likely so",
                "Yes",
                "You're on your own buddy",
                "Have you ever solved an exercise by yourself? 🤔",
                "Yes, EZ",
                "Always the same people 😒",
            ])


        return None
