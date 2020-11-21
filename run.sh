#!/bin/bash

# download language resources
snips-nlu download en

# generate dataset
snips-nlu generate-dataset en nlu-dataset.yaml > /tmp/nlu-dataset.json 

# run bot
python main.py $DISCORD_API_TOKEN --nlu-dataset /tmp/nlu-dataset.json --logfile bot.log