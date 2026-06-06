import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")

frm_converter = tk.Frame(root)
frm_converter.pack(padx=10, pady=10)

lbl_celsius = tk.Label(frm_converter, text="Celsius:")
lbl_celsius.grid(row=0, column=0, padx=5, pady=5, sticky="e")

ent_celsius = tk.Entry(frm_converter, width=15)
ent_celsius.grid(row=0, column=1, padx=5, pady=5)

lbl_result = tk.Label(frm_converter, text="Result will appear here")
lbl_result.grid(row=1, column=0, columnspan=3, padx=5, pady=10)


def convert_temperature():
    celsius_text = ent_celsius.get()
    fahrenheit = (float(celsius_text) * 9 / 5) + 32
    lbl_result["text"] = f"{fahrenheit:.1f} °F"


btn_convert = tk.Button(frm_converter, text="Convert", command=convert_temperature)
btn_convert.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
