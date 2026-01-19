def main():
    print(convert(str(input(''))))


def convert(emoji):
    return(emoji.replace(":)","🙂").replace(":(","🙁"))
    


main()
