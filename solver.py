# import requests
import json
from itertools import permutations

# def get(word):
#     url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
#     data = url.text
#     parseJson = json.loads(data)
#     try:
#         if parseJson["title"] == "No Definitions Found":
#             return False
#     except:
#         return True
#     # return parseJson[0]["meanings"][0]["partOfSpeech"]

def makeintoset():
    f = open("words_alpha.txt")
    g = set()
    for i in f:
        g.add(i.strip())
    return g


def getWord(shuffle, g):
    perm = ["".join(p) for p in set(permutations(shuffle))]
    for i in perm:
        if i in g:
            return i
    return "You entered the word wrongus"

