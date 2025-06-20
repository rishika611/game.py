import tkinter as tk
from tkinter import ttk, messagebox

# Define the main application class
class SimpleLengthConverterApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        master.title("Simple Length Converter")
        master.geometry("450x250") # Adjust initial window size

        # Define conversion factors for various units relative to meters
        self.units = {
            "Meter": 1.0,
            "Kilometer": 1000.0,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        }
        self.unit_names = list(self.units.keys())

        # --- Setup the Converter UI ---
        self.setup_converter_ui()

    def setup_converter_ui(self):
        # Frame for input widgets
        input_frame = ttk.LabelFrame(self.master, text="Convert Length")
        input_frame.pack(pady=15, padx=20, fill="x")

        # Value Entry
        ttk.Label(input_frame, text="Value:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.value_entry = ttk.Entry(input_frame)
        self.value_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # From Unit Dropdown
        ttk.Label(input_frame, text="From:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.from_unit_var = tk.StringVar(self.master)
        self.from_unit_var.set("Meter")
        self.from_unit_menu = ttk.Combobox(input_frame, textvariable=self.from_unit_var, values=self.unit_names, state="readonly")
        self.from_unit_menu.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # To Unit Dropdown
        ttk.Label(input_frame, text="To:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.to_unit_var = tk.StringVar(self.master)
        self.to_unit_var.set("Kilometer")
        self.to_unit_menu = ttk.Combobox(input_frame, textvariable=self.to_unit_var, values=self.unit_names, state="readonly")
        self.to_unit_menu.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Expand the second column
        input_frame.columnconfigure(1, weight=1)

        # Convert Button
        convert_button = ttk.Button(self.master, text="Convert", command=self.convert_length)
        convert_button.pack(pady=10)

        # Result Label
        self.result_label = ttk.Label(self.master, text="Result will appear here.", font=("Arial", 11))
        self.result_label.pack(pady=5)

    def convert_length(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            if from_unit == to_unit:
                messagebox.showinfo("Conversion Info", "Units are the same. No conversion needed.")
                self.result_label.config(text=f"{value} {from_unit}")
                return

            value_in_meters = value * self.units[from_unit]
            converted_value = value_in_meters / self.units[to_unit]

            self.result_label.config(text=f"{value} {from_unit} = {converted_value:.4f} {to_unit}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
        except KeyError as e:
            messagebox.showerror("Error", f"An unexpected unit was selected: {e}")

# --- Main part of the script ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleLengthConverterApp(root)
    root.mainloop()