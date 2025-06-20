import solver
import tkinter as tk
import jumbleGuiCommands as jgc
# Defining all the setup stuff here or smth...
root = tk.Tk()
# root.geometry("800x500")
root.title('Jumble Solver 😀😀😀')

# Gonna be defining some variables here or smth...
word1 = tk.StringVar()


# Actual widget organization goes here : (!?/!?!?!?!/!?!?!?!??!?!?)
header = tk.Label(root, text="This is the jumble solver GUI! For each box, enter the scrambled words... (Other instructions later)", font=("Arial", 16, "bold"), padx = 15, pady = 15)
header.pack()

firstWord = tk.Entry(root, text="Scrambled Word", font=('calibre', 10, 'bold'))
process1=tk.Button(root,text = 'Submit', command = solver.getWord(firstWord.get()))
answer1 = tk.Label(root, text="")


root.mainloop()