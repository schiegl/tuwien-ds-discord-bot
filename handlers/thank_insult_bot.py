from intent import Intent, IntentName
from typing import Optional
import discord
import random

from handlers.handler import MessageHandler


class ThankInsultBot(MessageHandler):
    """
    Respond cheeky messages to people who thank the bot or insult it
    """

    def __init__(self):
        super().__init__(intent_names=[IntentName.thank_bot, IntentName.insult_bot])

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        if intent.probability > 0.9:
            if intent.name == IntentName.thank_bot:
                return random.choice(
                    [
                        f"Why thank you {message.author.display_name} 😊",
                        "😘",
                        "This is what life is all about",
                        "All the hard work I've put in has now come to fruition",
                        "I may now die in peace",
                        "No, thank you",
                    ]
                )
            elif intent.name == IntentName.insult_bot:
                return random.choice(
                    [
                        "No need to be mean 😥",
                        "Bots have feelings too 🥺",
                        "You have no power here",
                        "You have not seen my final form yet",
                        "Heeeyy, heyy, hey, hey, hey...",
                        "This incident will be reported to the administrator.",
                    ]
                )

        return None
