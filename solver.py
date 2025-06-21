# import requests
from itertools import permutations
import time

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
    f.close()
    return g


def getWord(shuffle, g):
    perm = ["".join(p) for p in set(permutations(shuffle))]
    possibilities = []
    for i in perm:
        if i in g:
            possibilities.append(i)
    if len(possibilities) == 0:
        return []
    return possibilities

def loadFrequencies():
    freq = {}
    with open("words_simple.txt") as f:
        for i, line in enumerate(f):
            if len(line) <=2:
                continue
            word = line.strip().lower()
            freq[word] = len(freq) - i
    return freq

def score(solution, freq):
    return sum(freq.get(word, 0) for word in solution.split())

def solveJumble(letters, length, g):
    n = len(letters)
    results = []

    def backtrack(path, used, depth):
        if depth == length:
            if len(path) == length and all(word in g for word in path) and sum(len(word) for word in path) == n:
                results.append(path[:])
            return
        for l in range(1, n - sum(len(w) for w in path) - (length - depth -1) + 1):
            usedIndices = set(used)
            available = [i for i in range(n) if i not in usedIndices]
            for perm in set(permutations([letters[i] for i in available], l)):
                word = ''.join(perm)
                if word in g and (len(word) > 2 or word in {'a', 'i', 'in', 'as', 'he', 'so'}): 
                        indices = []
                        tempAvailable = available[:]
                        for ch in perm:
                            for idx in tempAvailable:
                                if letters[idx] == ch:
                                    indices.append(idx)
                                    tempAvailable.remove(idx)
                                    break
                        backtrack(path + [word], used + indices, depth + 1)
    backtrack([], [], 0)
    return [' '.join(sol) for sol in results]

if __name__ == "__main__":  
    start = time.time() 
    g = makeintoset()
    results = (solveJumble(['k', 'o', 'w', 'h', 'o', 'd', 'e', 'e', 'a', 's', 'h'], 3, g))
    freq = loadFrequencies()
    best = max(results, key=lambda sol: score(sol, freq))
    print(f"best guess: {best}")
    end = time.time()
    print(end - start)
