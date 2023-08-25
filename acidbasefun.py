import math

def acidbasefun(c):
    pH = -math.log(c, 10)
    
    if pH < 7:
        return 'Acidic!'
    
    elif pH == 7:
        return 'Netural like water'

    else:
        return 'Basic!'

con = input("Enter Concentration (in scientific notation, e.g., 1e-10): ")
c = float(con)

result = acidbasefun(c)

print("Wow, it's so", result)