import tkinter as tk
from calculator import elevation_calc

def show_value():
    try:
        distance = float(entry.get())
        elevation, powder_charges = elevation_calc(distance)
        print(f"Distance to target: {distance}")
        print(f"Elevation: {elevation}")
        print(f"Powder Charges: {powder_charges}")
    except ValueError:
        print("Value provided is not a float number")

root = tk.Tk()

label = tk.Label(root, text="Distance (km):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show", command=show_value)
button.pack()

root.mainloop()