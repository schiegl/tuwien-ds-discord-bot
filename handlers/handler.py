from abc import ABC, abstractmethod
from intent import Intent, IntentName
from typing import List, Optional
import discord
from collections import defaultdict
from datetime import datetime


class MessageHandler(ABC):
    def __init__(self, channels: List[str] = [], intent_names: List[IntentName] = [], timeout=0):
        """
        :param channels: The channels that this handler will listen to (if empty then all channels)
        :param intent_names: The intents that this handler will listen to (if empty then all intents)
        :param timeout: The seconds before this handler is active again (per channel)
        """
        self.channels = set(channels)
        self.intent_names = set(intent_names)
        self.timeout = timeout
        self._last_time_executed = defaultdict(lambda: datetime.fromtimestamp(0))

    def __call__(self, message: discord.Message, intent: Intent) -> Optional[str]:
        matching_channel = not self.channels or message.channel.name in self.channels
        matching_intent = not self.intent_names or intent.name in self.intent_names

        if matching_channel and matching_intent:
            last_time = self._last_time_executed[message.channel.name]
            if (message.created_at - last_time).total_seconds() >= self.timeout:
                self._last_time_executed[message.channel.name] = message.created_at
                return self.handle(message, intent)

        return None

    @abstractmethod
    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        """Handle a message sent by a user

        :param message: Discord message
        :param intent: Intent detected by Snips NLU
        :return: Response to message or None
        """
        pass
