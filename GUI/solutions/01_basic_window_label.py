import tkinter as tk

root = tk.Tk()
title = "Basic Window with Label"
root.title(title)
root.geometry("300x200")
lbl = tk.Label(root, text="Gomycode")
lbl.pack()

root.mainloop()
