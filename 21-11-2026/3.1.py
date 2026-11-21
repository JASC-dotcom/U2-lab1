# Jose Antonio Santiago Cabrera - 3.1.py

for n in range(1, 51):
    if n % 3 == 0:
        continue                 # skip multiples of 3
    if n % 17 == 0 and n > 20:
        break                    # first multiple of 17 greater than 20
    print(n)