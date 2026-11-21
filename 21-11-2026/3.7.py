# Jose Antonio Santiago Cabrera - 3.7.py

largest = None
smallest = None

while True:
    text = input("Integer (or 'end'): ").strip()
    if text == "end":
        break
    try:
        number = int(text)
    except ValueError:
        print("Warning: type an integer or 'end'")
        continue

    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

if largest is None:
    print("No numbers were entered")
else:
    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")