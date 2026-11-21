# Jose Antonio Santiago Cabrera - 3.3.py

try:
    number = int(input("Integer: "))
except ValueError:
    print("That is not a valid number")
else:
    print(f"You typed {number}")