# Jose Antonio Santiago Cabrera - 3.6a.py
# Version A: raises the exception and does NOT catch it (the program stops
# with a traceback when the value is out of range).

cpu = float(input("CPU usage (%): "))

if not 0 <= cpu <= 100:
    raise ValueError("CPU usage must be between 0 and 100")

print(f"CPU usage: {cpu}%")