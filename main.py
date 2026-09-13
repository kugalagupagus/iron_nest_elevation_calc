import tkinter as tk

def elevation_calc(distance):
    max_elevation = 60
    if distance <= 10:
        powder_charges = 1
    elif distance <= 20:
        powder_charges = 2
    elif distance <= 30:
            powder_charges = 3
    elif distance <= 40:
            powder_charges = 4
    elif distance <= 50:
            powder_charges = 5
    else:
          powder_charges = 6
    elevation = (distance * max_elevation) / (powder_charges * 10)
    return elevation, powder_charges

def show_value():
    try:
          distance = float(entry.get())
          elevation, powder_charges = elevation_calc(distance)
          print(f"Distance to target: {distance}")
          print(f"Elevation: {elevation}")
          print(f"Powder Charges: {powder_charges}")
    except ValueError:
          print("Value povided is not a float number")

root = tk.Tk()

label = tk.Label(root, text="Distance (km):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show", command=show_value)
button.pack()

root.mainloop()