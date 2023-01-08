import discord
import os
import requests
import json
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

    if message.content.startswith(".hello"):
        await message.channel.send("lo con cac")

    if message.content.startswith(".goodbye"):
        await message.channel.send("khong ai nhan tin nen di ngu? chu' j 🙄")

    if message.content.startswith("da. god"):
        await message.channel.send("toi qua' gae")

    if message.content.startswith("bot oi"):
        await message.channel.send("j")

    if message.content.startswith("bun`"):
        await message.channel.send("vui len di")

    if message.content.startswith("vui kieu j"):
        await message.channel.send("suc cac")

    if message.content.startswith(".dict integrity"):
        word = getWord()
        await message.channel.send(word)

client.run(TOKEN)