import requests
import json
# word = jsonData[0]["word"]
# wordPhonetic = jsonData[0]["phonetics"]
# wordMeaning = jsonData[0]["meanings"]


# for result in wordMeaning:
#     print(result["definitions"][0]["definition"])
#     for result2 in result["definitions"]:
#         print(result2["definition"])

def findWord(wordInput):
    wordReturn = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(wordInput))
    jsonData = json.loads(wordReturn.text)
    print(jsonData)
