import tkinter as tk

root = tk.Tk()
root.title("Entry Widget")

entry = tk.Entry(root, width=40)
entry.pack()
entry.insert(0, "What is your name?")

root.mainloop()
