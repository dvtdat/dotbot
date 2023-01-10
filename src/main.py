import discord
import os
import requests
import json
import re
from dotenv import load_dotenv  # pip install python-dotenv, required to load TOKEN from .env

from dict import findWord

load_dotenv()

TOKEN = os.getenv('TOKEN')
prefix = "dot"
client = discord.Client(intents = discord.Intents.all())

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def embed(message, user:discord.member = None):
    # if user == None:
    #     user = user.author
    
    # userName = user.display_name
    # userAvatar = user.display_avatar

    embedOutput = discord.Embed(title = "Hello", description = "Fuck you", color = 0x992d22)
    await message.channel.send(embed = embedOutput)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messageContentLowercase = message.content.lower()
    
    if (messageContentLowercase == "embed"):
        await embed(message)

    if (messageContentLowercase == "{} ping".format(prefix)):
        await message.reply(f"pong! {round(client.latency * 1000)} ms")

    if (messageContentLowercase.find("da. god") != -1 or messageContentLowercase.find("dạ god") != -1 ):
        await message.reply("toi qua' gae")

    if (re.search(r"^({}) (\w+)".format(prefix), messageContentLowercase)):
        userRequest = re.findall(r"^({}) (\w+)".format(prefix), messageContentLowercase)[0][1]
        
        if (userRequest == "hello" or userRequest == "hi"):
            await message.channel.send("hi")
        
        if (userRequest == "bye" or userRequest == "goodbye"):
            await message.channel.send("pp")

        if (userRequest == "dictionary" or userRequest == "dict"):
            userWord = re.findall(r"^({}) (\w+) (\w+)".format(prefix), messageContentLowercase)[0][2]
            await findWord(userWord, message)






    
client.run(TOKEN)