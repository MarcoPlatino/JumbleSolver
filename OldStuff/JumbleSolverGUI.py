import solver
import tkinter as tk
import OldStuff.jumbleGuiCommands as jgc

# Preparing all of the window stuff
root = tk.Tk()
root.title('Jumble Solver 😀😀😀')
g = solver.makeintoset()

# Declaring variables
word1 = tk.StringVar()

# Window headers
header = tk.Label(root, text="This is the jumble solver GUI! For each box, enter the scrambled words... (Other instructions later)", font=("Arial", 16, "bold"), padx=15, pady=15)
header.grid(row = 0, column= 1)

# Defining all the functions for the stuff
def onSubmit():
    print("click!!!")
    scramble = word1.get()
    answer = solver.getWord(scramble, g)
    print(answer)
    answer1.config(text=answer)
    word1.set("")


firstWord = tk.Entry(root, textvariable=word1, font=('calibre', 10, 'bold'))

firstWord.grid(row = 1, column = 0)

answer1 = tk.Label(root, text="Nothing here until you enter the word 😀")
answer1.grid(row = 1, column = 1)

process1 = tk.Button(root, text='Submit', command=onSubmit)
process1.grid(row = 2, column = 0)

root.mainloop()
