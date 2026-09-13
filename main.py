import tkinter as tk
import keyboard
from calculator import elevation_calc
from window_controls import WindowToggler

def show_value():
    distance_label.pack_forget()
    elevation_label.pack_forget()
    powder_charges_label.pack_forget()
    status_label.pack_forget()
    try:
        distance = float(entry.get().replace(",", "."))
        elevation, powder_charges = elevation_calc(distance)
        distance_label.pack(before=entry)
        elevation_label.pack(before=entry)
        powder_charges_label.pack(before=entry)
        distance_label.configure(text=f"{distance}")
        elevation_label.configure(text=f"Elevation: {round(elevation, 2)}")
        powder_charges_label.configure(text=f"Powder Charges: {powder_charges}")
    except ValueError:
        status_label.pack(before=entry)
        status_label.configure(text="Value provided is not a float number")

root = tk.Tk()

toggler = WindowToggler(root)

root.attributes('-topmost', True)
root.resizable(False, False)
root.geometry("300x250")

label = tk.Label(root, text="Distance (km):")
label.pack()

status_label = tk.Label(root, text="")

distance_label = tk.Label(root, text="")

elevation_label = tk.Label(root, text="")

powder_charges_label = tk.Label(root, text="")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show", command=show_value)
button.pack()

keyboard.add_hotkey('f8', toggler.on_hotkey)

root.mainloop()