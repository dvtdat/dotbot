import requests
import json
import discord
from word import *

async def findWord(wordInput, message):
    jsonRequest = json.loads(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(wordInput)).text)
    
    if "title" in jsonRequest:
        await message.channel.send("Mie-san couldn't find your word :cry:")
        return

    jsonData = jsonRequest[0]
    word = Word(jsonData["word"])

    for inputPhonetic in jsonData["phonetics"]:
        if "text" in inputPhonetic:
            word.addPhonetic(inputPhonetic["text"], ("N/A" if "sourceUrl" not in inputPhonetic else inputPhonetic["sourceUrl"]))

    for inputMeaning in jsonData["meanings"]:
        for inputDefinition in inputMeaning["definitions"]:
            word.addMeaning(inputMeaning["partOfSpeech"], inputDefinition["definition"])

    await message.channel.send(word.term)
    for newWordPhonetic in word.phonetic:
        await message.channel.send(newWordPhonetic.text)

    for newWordMeaning in word.meaning:
        await message.channel.send(newWordMeaning.POS + " - " + newWordMeaning.definition)

