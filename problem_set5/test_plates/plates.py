def main():
    plate = input("plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")


def Two_char(s):
    return s[0:2].isalpha()


def length_correct(s):
    return 2 <= len(s) <=6

def correct_digit(s):
    if not any(char.isdigit()for char in s):
        return True
    digits_start = False 
    for char in s:
        if char.isdigit():
            digits_start = True
        elif digits_start:
            return False
    return True


def not_zero(s):
    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            else:
                return True
    return True

def special_symbols(s):
    symbols = ['#','@','!','$','%','^','&','*','(',')','_','-','=','+']
    return not any(ch in symbols for ch in s)
def is_valid(s):
     return all ([Two_char(s) and  length_correct(s) and correct_digit(s) and not_zero(s)and special_symbols(s)])
if __name__ == "__main__":
    main()

