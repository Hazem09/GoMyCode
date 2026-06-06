import tkinter as tk

root = tk.Tk()
root.title("Custom Label and Button")

lbl = tk.Label(root, text="Tkinter", bg="black", fg="white", width=10, height=10)
btn = tk.Button(root, text="Click me!", bg="blue", fg="yellow", activebackground="red", activeforeground="black")
lbl.pack()
btn.pack()

root.mainloop()
