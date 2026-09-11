def elevation_calc(distance, powder_charges):
    max_elevation = 60
    elevation = (distance * max_elevation) / (powder_charges * 10)
    return elevation

distance = float(input("Enter distance to target:"))
powder_charges = float(input("Enter number of powder charges:"))

print(elevation_calc(distance, powder_charges))