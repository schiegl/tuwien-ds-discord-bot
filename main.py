from typing import List
from argparse import ArgumentParser
import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
import discord
import logging
import sys
import re

from handlers.handler import MessageHandler
from handlers.english_only import EnglishOnly
from handlers.code_format import CodeFormatReminder
from handlers.play_among_us import PlayAmongUs
from handlers.wise_quote import TellWiseQuote
from handlers.thank_insult_bot import ThankInsultBot
from handlers.anyone_solved import AnyoneSolved
from intent import Intent, IntentName


argparser = ArgumentParser(description="Run the Discord bot")
argparser.add_argument("discord_api_token", help="API Token for Discord bot")
argparser.add_argument("--nlu-dataset", help="Path to json dataset to learn from")
argparser.add_argument("--debug", help="Whether to log everything", action="store_true")
args = argparser.parse_args()


def get_logger() -> logging.Logger:
    logger = logging.getLogger("discord")
    log_format = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")

    logger.setLevel(logging.DEBUG if args.debug else logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_format)
    logger.addHandler(handler)

    return logger


def get_nlu_engine(dataset_json_path: str) -> SnipsNLUEngine:
    with io.open(dataset_json_path) as f:
        dataset = json.load(f)

    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine = nlu_engine.fit(dataset)
    return nlu_engine


snips = get_nlu_engine(args.nlu_dataset)
logger = get_logger()

client = discord.Client(
    intents=discord.Intents(
        messages=True,  # receive messages
        members=True,  # send messages to users
        guilds=True,  # send messages to channels
    ),
)

# all the handlers that will be run for each message
handlers: List[MessageHandler] = [
    EnglishOnly(),
    CodeFormatReminder(),
    ThankInsultBot(),
    PlayAmongUs(),
    AnyoneSolved(),
    TellWiseQuote(),
]


@client.event
async def on_ready():
    logger.info("Connected guilds")
    for guild in client.guilds:
        logger.info(f" - {guild.id} (name: {guild.name})")


@client.event
async def on_member_join(member: discord.Member):
    try:
        await member.send(
            "Welcome to the TU Data Science & Friends server! Please look at the #info-and-rules channel to get settled in e.g. get extra permissions."
        )
    except:
        logger.error("Failed to send DM to new member: ", member.display_name)


@client.event
async def on_message(message: discord.Message):
    # avoid responding to itself
    if message.author.bot:
        return

    # replace mentions with something snips can recognize
    clean_text = message.content.replace(f"<@!{client.user.id}>", "@bot")
    result = snips.parse(clean_text)
    intent_name = IntentName(result["intent"]["intentName"])
    intent = Intent(name=intent_name, probability=result["intent"]["probability"])

    for handler in handlers:
        response = handler(message, intent)
        if response:
            await message.channel.send(response)
            break


if __name__ == "__main__":
    client.run(args.discord_api_token)
