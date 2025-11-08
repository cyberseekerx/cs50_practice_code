def main():
    while True:
        try:
            fuel = (input("Fraction: "))
            x = convert(fuel)
            break
        except (ValueError,ZeroDivisionError):
            continue
    gauge(x) 



def convert(fraction):
    x,y = fraction.split("/")
    if int(y) == 0 or x > y:
        raise ValueError
    return round((int(x) / int(y))*100)
    





def gauge(percentage):
    x = percentage
    if x <= 1:
        print('E')
    elif x >= 99:
        print("F")
    else:
        print(f"{x}%")
    










if __name__ == "__main__":
    main()
