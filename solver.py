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

def makeintoset():
    f = open("words_alpha.txt")
    g = set()
    for i in r:
        g.add(i)
    return g


def getWord(shuffle):
    perm = ["".join(p) for p in set(permutations(shuffle))]


