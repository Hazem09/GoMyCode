import tkinter as tk

root = tk.Tk()
root.title("Address Form")

labels = [
    "First Name",
    "Last Name",
    "Street Address",
    "City",
    "State",
    "Zip Code",
    "Country",
]

frm_form = tk.Frame(root)
frm_form.pack(padx=10, pady=10)

frm_buttons = tk.Frame(root)
frm_buttons.pack(fill=tk.X, padx=10, pady=(0, 10))

for row, text in enumerate(labels):
    lbl = tk.Label(frm_form, text=text)
    ent = tk.Entry(frm_form, width=30)
    lbl.grid(row=row, column=0, sticky="e", padx=5, pady=5)
    ent.grid(row=row, column=1, padx=5, pady=5)

btn_submit = tk.Button(frm_buttons, text="Submit")
btn_clear = tk.Button(frm_buttons, text="Clear")
btn_submit.pack(side=tk.RIGHT, padx=(5, 0))
btn_clear.pack(side=tk.RIGHT)

root.mainloop()
