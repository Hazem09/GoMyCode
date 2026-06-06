import random
import tkinter as tk

root = tk.Tk()
root.title("Die Roller")

root.columnconfigure(0, minsize=200)
root.rowconfigure(0, minsize=50)
root.rowconfigure(1, minsize=50)

lbl_result = tk.Label(root, text="")


def roll():
    lbl_result["text"] = str(random.randint(1, 6))


btn_roll = tk.Button(root, text="Roll", command=roll)

btn_roll.grid(row=0, column=0, padx=10, pady=10)
lbl_result.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
