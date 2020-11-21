from dataclasses import dataclass
from enum import Enum


class IntentName(Enum):
    """
    Names must be exactly as in the YAML file
    """

    play_among_us = "play_among_us"
    insult_bot = "insult_bot"
    thank_bot = "thank_bot"
    tell_wise_quote = "tell_wise_quote"
    none = None


@dataclass
class Intent:
    name: IntentName
    probability: float