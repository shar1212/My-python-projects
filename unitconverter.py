import math

# SI to cgs converter

command = input("Enter unit type to convert: ")
if command.lower() == "mass":
    mass = float(input("Enter amount of grams to convert to kilograms: "))
    mass /= 1000
    mass = round(mass)
    print(f"{mass} kilograms")
elif command.lower() == "length":
    length = float(input("Enter amount of length meters to inches"))
    length *= 39.37
    print(f"{length} in inches")
elif command.lower() == "temp":
    temp = float(input("Enter kelvin tempature to convert to celcius"))
    temp -= 273.15
    temp = round(temp)
    print(f"{temp} celcius degrees")
elif command.lower() == "volume":
    volume = float(input("Enter amount of m3 to convert to liters"))
    volume *= 10**3
    print(f"The volume in liters is {volume}")


else:
    print("Invalid unit type. Please try again.")

print(command)
