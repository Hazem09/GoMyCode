import random
import tkinter as tk

root = tk.Tk()
root.title("Die Roller")

# TODO: set up the column and row minimum sizes using columnconfigure and rowconfigure
root.columnconfigure(0, minsize=200)
root.rowconfigure(0, minsize=50)
root.rowconfigure(1, minsize=50)

lbl_result = tk.Label(root, text="")


def roll():
    # TODO: update lbl_result["text"] with a random number


# TODO: create the button and link it to the roll function using the command parameter


# TODO: grid both the button and the empty result label


root.mainloop()
