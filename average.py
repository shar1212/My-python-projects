import math

num = 0
tot = 0.0
squared_diff_sum = 0.0

while True:
    sval = input('Enter a number: ')
    
    if sval == "done":
        break
    
    try:
        fval = float(sval) 
    except ValueError:
        print("Invalid input")
        continue
    
    num += 1
    tot += fval
    average = tot / num
    squared_diff_sum += (fval - average) ** 2

if num > 0:
    sol = math.sqrt(squared_diff_sum / num)
else:
    sol = 0.0  

print("Total:", tot)
print("Count:", num)
print("Average:", average)
print("Standard Deviation:", sol)