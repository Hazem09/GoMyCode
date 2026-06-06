import tkinter as tk
from tkinter import messagebox, ttk


class ElectricityCalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Electricity Cost Calculator")
        self.root.geometry("600x450")
        self.root.minsize(500, 350)

        # Ensure the root window expands properly
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Main wrapper frame
        outer_frame = ttk.Frame(self.root, padding=10)
        outer_frame.grid(row=0, column=0, sticky="nsew")
        outer_frame.columnconfigure(0, weight=1)
        outer_frame.rowconfigure(0, weight=1)

        # Canvas and Scrollbar to handle dynamic rows smoothly
        self.canvas = tk.Canvas(outer_frame, borderwidth=0, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(
            outer_frame, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Update scroll region whenever widgets are added/removed
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="nw"
        )

        # Ensure the scrollable interior expands to match canvas/window width
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Layout Canvas & Scrollbar
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Bind mouse wheel for scrolling convenience
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        # List to keep track of appliance inputs
        self.appliances = []

        # Bottom fixed panel (stays visible even when scrolling)
        self.control_panel = ttk.Frame(outer_frame, padding=10)
        self.control_panel.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.control_panel.columnconfigure(0, weight=1)
        self.control_panel.columnconfigure(1, weight=1)

        # Buttons
        self.add_button = ttk.Button(
            self.control_panel, text="+ Add Appliance", command=self.add_appliance
        )
        self.add_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.calc_button = ttk.Button(
            self.control_panel, text="Calculate Cost", command=self.calculate_cost
        )
        self.calc_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Result display
        self.result_label = ttk.Label(
            self.control_panel,
            text="Estimated Monthly Cost: $0.00",
            font=("Arial", 11, "bold"),
        )
        self.result_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Initialize with 4 default appliances as requested
        for _ in range(4):
            self.add_appliance()

    def _on_canvas_configure(self, event):
        # Stretches the dynamic interior frame to the width of the main window
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event):
        # Enable scroll wheel anywhere inside the window
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def add_appliance(self):
        # Create elements for a single appliance row
        label = ttk.Label(self.scrollable_frame, text="")
        p_lbl = ttk.Label(self.scrollable_frame, text="Power (W):")
        p_entry = ttk.Entry(self.scrollable_frame)
        t_lbl = ttk.Label(self.scrollable_frame, text="Hours/Day:")
        t_entry = ttk.Entry(self.scrollable_frame)

        # Individual row deletion button
        del_btn = ttk.Button(self.scrollable_frame, text="✕", width=3)

        app_dict = {
            "label": label,
            "p_lbl": p_lbl,
            "p_entry": p_entry,
            "t_lbl": t_lbl,
            "t_entry": t_entry,
            "del_btn": del_btn,
        }

        # Configure delete button to target this specific row
        del_btn.config(command=lambda: self.remove_appliance(app_dict))

        self.appliances.append(app_dict)
        self.rebuild_grid()

    def remove_appliance(self, app_dict):
        # Destroy widgets physically
        for widget in app_dict.values():
            widget.destroy()

        self.appliances.remove(app_dict)
        self.rebuild_grid()

    def rebuild_grid(self):
        # Temporarily clear placements to avoid overlapping grids
        for app in self.appliances:
            for widget in app.values():
                widget.grid_forget()

        # Place current rows back in clean order
        for index, app in enumerate(self.appliances):
            app["label"].config(text=f"Appliance {index + 1}")

            app["label"].grid(row=index, column=0, padx=5, pady=5, sticky="w")
            app["p_lbl"].grid(row=index, column=1, padx=2, pady=5, sticky="e")
            app["p_entry"].grid(
                row=index, column=2, padx=5, pady=5, sticky="ew"
            )
            app["t_lbl"].grid(row=index, column=3, padx=2, pady=5, sticky="e")
            app["t_entry"].grid(
                row=index, column=4, padx=5, pady=5, sticky="ew"
            )
            app["del_btn"].grid(row=index, column=5, padx=5, pady=5)

        # Allow the text input columns (2 and 4) to expand when resizing
        self.scrollable_frame.columnconfigure(2, weight=1)
        self.scrollable_frame.columnconfigure(4, weight=1)

    def calculate_cost(self):
        if not self.appliances:
            messagebox.showwarning(
                "Warning", "Please add at least one appliance to compute."
            )
            return

        total_daily_kwh = 0.0

        for index, app in enumerate(self.appliances):
            p_raw = app["p_entry"].get().strip()
            t_raw = app["t_entry"].get().strip()

            # Error Handling 1: Empty Fields
            if not p_raw or not t_raw:
                messagebox.showerror(
                    "Validation Error",
                    f"Appliance {index + 1} fields cannot be empty.",
                )
                return

            # Error Handling 2: Ensure Inputs are Numbers
            try:
                P = float(p_raw)
                t = float(t_raw)
            except ValueError:
                messagebox.showerror(
                    "Validation Error",
                    f"Appliance {index + 1} values must be valid numbers.",
                )
                return

            # Error Handling 3: Validate Physical Parameters
            if P < 0 or t < 0:
                messagebox.showerror(
                    "Validation Error",
                    f"Appliance {index + 1} values cannot be negative.",
                )
                return
            if t > 24:
                messagebox.showerror(
                    "Validation Error",
                    f"Appliance {index + 1} active hours cannot exceed 24 per day.",
                )
                return

            total_daily_kwh += (P * t) / 1000.0

        # Billing Fix: Cumulative monthly tiers
        # Applying tier limits to cumulative monthly consumption makes billing calculations realistic.
        monthly_kwh = total_daily_kwh * 30

        # Tier 1 (0 - 125 kWh) at $0.20
        if monthly_kwh <= 125:
            cost = monthly_kwh * 0.20
        # Tier 2 (126 - 250 kWh) at $0.30
        elif monthly_kwh <= 250:
            cost = (125 * 0.20) + ((monthly_kwh - 125) * 0.30)
        # Tier 3 (251+ kWh) at $0.50
        else:
            cost = (125 * 0.20) + (125 * 0.30) + ((monthly_kwh - 250) * 0.50)

        self.result_label.config(text=f"Estimated Monthly Cost: ${cost:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ElectricityCalculatorApp(root)
    root.mainloop()