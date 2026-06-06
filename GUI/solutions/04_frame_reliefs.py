import tkinter as tk

root = tk.Tk()
root.title("Frame Reliefs")

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief_style in border_effects.items():
    frame = tk.Frame(root, relief=relief_style, borderwidth=5)
    frame.pack(side=tk.LEFT, padx=5, pady=5)

    label = tk.Label(frame, text=relief_name)
    label.pack(padx=10, pady=10)

root.mainloop()
