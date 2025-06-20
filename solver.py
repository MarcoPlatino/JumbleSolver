import requests
import json
from itertools import permutations

def get(word):
    url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = url.text
    parseJson = json.loads(data)
    try:
        if parseJson["title"] == "No Definitions Found":
            return False
    except:
        return True
    # return parseJson[0]["meanings"][0]["partOfSpeech"]

def getWord(shuffle):
    perm = ["".join(p) for p in permutations(shuffle)]
    for i in perm:
        if get(i):
            return i

