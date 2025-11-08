def main():
    greating = str(input("Greating: "))
    print(f"${value(greating)}")

def value(greating):
    lower_greating = greating.lower().lstrip(" ")
    if lower_greating.startswith("hello"):
        return  0
    elif lower_greating.startswith('h'):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()


