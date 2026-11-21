# Jose Antonio Santiago Cabrera - 3.6b.py
# Version B: catches the exception and asks again.

while True:
    try:
        cpu = float(input("CPU usage (%): "))
        if not 0 <= cpu <= 100:
            raise ValueError("CPU usage must be between 0 and 100")
    except ValueError as error:
        print(f"Invalid value: {error}")
    else:
        break

print(f"CPU usage: {cpu}%")