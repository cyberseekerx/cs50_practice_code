def main():
    fuel = (input("Fraction: "))
    x = convert(fuel)
    (gauge(x))



def convert(fraction):
    try:
        x,y = fraction.split("/")
        y = int(y)
        x = int(x)
        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y < 0:
            raise ValueError
        return round((x / y)*100)
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    





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
