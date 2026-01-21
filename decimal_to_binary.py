import sys

decimal = int(sys.argv[1])
bits = {128: 0, 64: 0, 32: 0, 16: 0, 8: 0, 4: 0, 2: 0, 1: 0}
for bit, value in bits.items():
    if decimal >= bit:
        decimal = decimal - bit
        value = +1
    print(f"{value}", end="")
