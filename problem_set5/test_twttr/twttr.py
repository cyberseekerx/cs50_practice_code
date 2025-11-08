def main():
    text = str(input("Input: "))
    print('Output:',shorten(text))

def shorten(word):
    l = ""
    vowels = ['a','e','i','o','u']
    for x in word:
        if x.lower() not in vowels:
            l += x
    return l
             






if __name__ == "__main__" :
    main()
