import eel
import solver

eel.init("web")  
g = solver.makeintoset()

# Exposing the random_python function to javascript
# @eel.expose    # This is a little example just to demonstrate how it ends up looking when you define a function in eel!!!
# def random_python():
#     print("Random function running")
#     return randint(1,100)

# # Start the index.html file


@eel.expose
def unScramble(word):
    print("Successful Call")
    
    return solver.getWord(word, g)

@eel.expose
def solve(letters):
    return solver.solveJumble(letters)

eel.start("index.html")
