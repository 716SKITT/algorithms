total_mass = 0
count = 0

while True:
    mass = float(input("enter mass (or 0 for exit): "))

    if mass == 0:
        break

    total_mass += mass
    count += 1

if count == 0:
    print("no data for math.")
else: 
    average_mass = total_mass / count
    print(f"sr.mass: {average_mass:.2f}")
