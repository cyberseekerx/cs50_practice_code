import inflect
p = inflect.engine()
Names = []
while True:
    try:
        name = input("Name: ")
        Names.append(name)
    except EOFError:
        break
print()
s = p.join((Names))
print(f"Adieu, adieu, to {s}")
