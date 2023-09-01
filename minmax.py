largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except ValueError:
        print("Invalid input")
        continue

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

if largest is not None:
    print("Maximum is", largest)

if smallest is not None:
    print("Minimum is", smallest)