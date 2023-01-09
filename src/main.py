import discord
import os
import requests
import json
import re
from dotenv import load_dotenv  # pip install python-dotenv, required to load TOKEN from .env

from dict import *

load_dotenv()

TOKEN = os.getenv('TOKEN')
prefix = "dot"
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageContentLowercase = message.content.lower()
    
    if (re.search(r"^({}) (\w+)".format(prefix), messageContentLowercase)):
        userRequest = re.findall(r"^({}) (\w+)".format(prefix), messageContentLowercase)[0][1]
        
        if (userRequest == "hello" or userRequest == "hi"):
            await message.channel.send("lo lo cai dit con me may")
        
        if (userRequest == "bye" or userRequest == "goodbye"):
            await message.channel.send("cut con me m di thg suc vat")

        if (userRequest == "dictionary" or userRequest == "dict"):
            userWord = re.findall(r"^({}) (\w+) (\w+)".format(prefix), messageContentLowercase)[0][2]
            findWord(userWord)

    if (messageContentLowercase.find("da. god") != -1 or messageContentLowercase.find("dạ god") != -1 ):
        await message.channel.send("toi qua' gae")


    
client.run(TOKEN)