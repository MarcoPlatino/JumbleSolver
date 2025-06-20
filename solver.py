import requests
import json

def get(word):
    url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = url.text
    parseJson = json.loads(data)
    # if parseJson["title"] == "No Definitions Found":
    #     return False
    return parseJson[0]["meanings"][0]["partOfSpeech"]

print(get("because"))