from intent import Intent
import re
from typing import Optional
import discord

from handlers.handler import MessageHandler


class CodeFormatReminder(MessageHandler):
    """
    If the message contains code that is not formatted this handler will respond with a reminder on how to format code in markdown.

    FIXME: very naive implementation, doesn't if space is missing before parens e.g. "this is a sentence(really)"
    """

    def __init__(self):
        # wait 10 minutes before running handler again
        super().__init__(timeout=10 * 60)

        self.detectors = {
            "function": re.compile(r"[\w_\.]+\(.{0,30}\)"),  # e.g. print()
            "sql_keywords": re.compile(r"(?:SELECT|FROM|GROUP|JOIN|EXIST|NOT|NULL)"),  # e.g. SELECT a FROM b
            "r_assign": re.compile(r"[\w\.\_]+\s?<-\s?[\w\.\_]+"),  # e.g. a <- 123
            "array_index": re.compile(r"[\w\.\_]+\[[\w,\-\":]+\]"),  # e.g. var_name[15,2]
            "latex": re.compile(r"\\{\}"),  # e.g. var_name[15,2]
            "python_keywords": re.compile(r"(?:try:|except:|else:|elif)"),
            "general_keywords": re.compile(r"(?:\=\=|\!\=|\<\=|\>\=|\+\=)"),  # e.g. a != b
            "latex_or_path": re.compile(r"\\\w+"),
            "curly_braces": re.compile(r"[\{\}]"),  # assuming that curly braces are only used in code
        }

    def handle(self, message: discord.Message, intent: Intent) -> Optional[str]:
        text = message.content
        for _, regex in self.detectors.items():
            if regex.search(text):
                return "Did you know that you can **format code** in your messages? To format *inline* use `` ` ``, for *code blocks* use `` ``` `` and to *syntax highlight* add the language name e.g. `` ```python ``."

        return None
