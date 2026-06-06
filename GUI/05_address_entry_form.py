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
# TODO: pack the button frame with fill=tk.X


for row, text in enumerate(labels):
    # TODO: create the Label and Entry widgets, then place them using .grid()


# TODO: create and pack the "Submit" and "Clear" buttons to the right


root.mainloop()
