def elevation_calc(distance):
    max_elevation = 60
    if distance <= 5:
        powder_charges = 1
    elif distance <= 10:
        powder_charges = 2
    elif distance <= 15:
        powder_charges = 3
    elif distance <= 20:
        powder_charges = 4
    elif distance <= 25:
        powder_charges = 5
    else:
        powder_charges = 6
    elevation = (distance * max_elevation) / (powder_charges * 5)
    return elevation, powder_charges

if __name__ == "__main__":
    distance = float(input("Enter distance to target:"))
    elevation, powder_charges = elevation_calc(distance)
    print(f"Elevation: {elevation}")
    print(f"Powder Charges: {powder_charges}")