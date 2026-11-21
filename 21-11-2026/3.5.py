# Jose Antonio Santiago Cabrera - 3.5.py

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    result = a / b
except ValueError:
    print("Please type valid numbers")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(f"Result: {result:.2f}")
finally:
    print("End of the operation")