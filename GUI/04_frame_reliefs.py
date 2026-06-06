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
    # TODO: create the frame with the correct relief and a borderwidth of 5
    

    # TODO: pack the frame to the left
    

    # TODO: create and pack the label inside the frame displaying the relief name


root.mainloop()
