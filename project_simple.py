import tkinter as tk
import numpy as np


def calculate_cost():
    # read 4 appliances power and time, compute total kWh
    total_kwh = 0.0
    for i in range(4):
        P = float(power_entries[i].get())
        t = float(time_entries[i].get())
        total_kwh += (P * t) / 1000.0
    kwh = total_kwh
    # 1st 125kwh at 0.20
    if kwh <= 125:
        cost = kwh * 0.20
    # 126-250kwh at 0.30
    elif kwh <= 250:
        cost = (125 * 0.20) + ((kwh - 125) * 0.30)
    # 251 and bigger at 0.50
    else:
        cost = (125 * 0.20) + (125 * 0.30) + ((kwh - 250) * 0.50)
    
    # monthly cost (daily usage * 30 days)
    monthly_cost = cost * 30
    return monthly_cost

window = tk.Tk()
window.title("Electricity Cost Calculator")

# create entries for 4 appliances
power_entries = []
time_entries = []
for i in range(4):
    # Frame for each appliance
    frame = tk.Frame(window)
    frame.pack()
    
    p_label = tk.Label(frame, text=f"Appliance {i+1} - Power (W):")
    p_label.pack(side=tk.LEFT, padx=5)
    p_entry = tk.Entry(frame, width=10)
    p_entry.pack(side=tk.LEFT, padx=5)
    power_entries.append(p_entry)

    t_label = tk.Label(frame, text=f"Time (hours/day):")
    t_label.pack(side=tk.LEFT, padx=5)
    t_entry = tk.Entry(frame, width=10)
    t_entry.pack(side=tk.LEFT, padx=5)
    time_entries.append(t_entry)

# Calculate button
calculate_button = tk.Button(window, text="Calculate Cost", command=lambda: result_label.config(text=f"Estimated Monthly Cost: ${calculate_cost():.2f}"))
calculate_button.pack()
# Result label
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()