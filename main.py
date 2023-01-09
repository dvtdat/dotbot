import discord
import os
import requests
import json
import re
from dotenv import load_dotenv  # pip install python-dotenv, required to load TOKEN from .env

load_dotenv()

TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.all())

def getWord():
    wordInput = "integrity"
    wordReturn = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(wordInput))
    jsonData = json.loads(wordReturn.text)

    word = jsonData[0]["word"]
    wordPhonetic = jsonData[0]["phonetics"]
    wordMeaning = jsonData[0]["meanings"]

    for result in wordPhonetic:
        if ("text" in result):
            return result["text"]

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageContent = message.content.lower()
    
    if (re.search(r"^(dot) (\w+)", messageContent)):
        userRequest = re.findall(r"^(dot) (\w+)", messageContent)[0][1]        
        if (userRequest == "hello" or userRequest == "hi"):
            await message.channel.send("lo lo cai dit con me may")
        if (userRequest == "bye" or userRequest == "goodbye"):
            await message.channel.send("cut con me m di thg suc vat")
    
client.run(TOKEN)