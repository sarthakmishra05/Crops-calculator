import tkinter as tk
from tkinter import ttk, messagebox

# Crop prices per kg (INR)
crop_prices = {
    "Wheat": 25,
    "Rice": 40,
    "Maize": 22,
    "Potato": 18,
    "Onion": 30,
    "Sugarcane": 4,
    "Soybean": 48,
    "Cotton": 65
}

def calculate_price():
    crop = crop_var.get()
    weight_text = weight_entry.get()

    if weight_text == "":
        messagebox.showerror("Input Error", "Please enter weight in kg!")
        return

    try:
        weight = float(weight_text)
    except ValueError:
        messagebox.showerror("Input Error", "Weight must be a number!")
        return

    price_per_kg = crop_prices[crop]
    total_price = price_per_kg * weight

    result_label.config(
        text=f"Crop: {crop}\n"
             f"Price per kg: ₹{price_per_kg}\n"
             f"Weight: {weight} kg\n"
             f"Total Price: ₹{total_price}"
    )


# Tkinter Window
root = tk.Tk()
root.title("Smart Crop Price Calculator")
root.geometry("350x350")
root.config(bg="#E6F7E6")

title_label = tk.Label(root, text="Smart Crop Price Calculator",
                       font=("Arial", 14, "bold"), bg="#E6F7E6")
title_label.pack(pady=10)

# Crop dropdown
crop_var = tk.StringVar()
crop_dropdown = ttk.Combobox(root, textvariable=crop_var, values=list(crop_prices.keys()))
crop_dropdown.current(0)
crop_dropdown.pack(pady=10)

# Weight input
weight_label = tk.Label(root, text="Enter Weight (kg):", bg="#E6F7E6", font=("Arial", 10))
weight_label.pack()

weight_entry = tk.Entry(root, font=("Arial", 11))
weight_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate Price", font=("Arial", 11, "bold"),
                        bg="#4CAF50", fg="white", width=20, command=calculate_price)
calc_button.pack(pady=15)

# Result display
result_label = tk.Label(root, text="", bg="#E6F7E6", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()