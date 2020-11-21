# TU Wien Data Science Discord Bot

This is the repository for the bot of the TU Wien Data Science Discord server.


## How it works?
The bot connects to Discord via [discord.py](https://github.com/Rapptz/discord.py) and parses messages with [snips](https://github.com/snipsco/snips-nlu). Every message that is sent on the server is passed to message handlers defined in `handlers/`. These message handlers decide if they want to respond to the given message themselves. In addition to the message the intent (extracted with snips) is also passed to each handler. Intents are defined in `nlu-dataset.yml` and may be extended.

For more info on intents, see [snips documentation](https://snips-nlu.readthedocs.io/en/latest/index.html).


## How to run?
If you'd like to run the bot e.g. on your own server for testing purposes you need your own API token.

```bash
# make api token available in environment
export DISCORD_API_TOKEN="<your-token>"

# make the script executable
chmod +x run.sh

# run the bot
./run.sh
```


## Contribute
There are a few ways you can contribute

### Add more expressions/responses (easy)
In `nlu-dataset.yaml` you will find the type of phrases the bot will be able to detect (called intents) and respond to. You can add more examples for each intent by just adding another bullet point. This will make the bot respond to a wider variety of phrases.

You can also add more responses. The responses can be found inside the message handlers themselves.

### Add/Improve message handlers and/or intents (medium)
In the directory `handler/` you will find different types of message handlers or actions of the bot. Each of them will do different things and respond to different intents. For example `handlers/english_only.py` will respond to messages that are German and remind people to keep the chat English.

### Extend/Improve architecture (hard)
If you want to do something that the current architecture doesn't support, create an issue on how you would like to improve it. If the idea makes sense and you can pull it off, I'll accept pull requests.
