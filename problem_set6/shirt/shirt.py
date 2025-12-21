import sys 
from PIL import Image

def main():
    cli_input()


def cli_input():
    if len(sys.argv) > 3:
        sys.exit(f'too many command-line arguments {len(sys.argv)}')
    elif len(sys.argv) < 3:
        sys.exit(f'too few command-line arguments {len(sys.argv)}')
    elif sys.argv[1].endswith(('.jpg','.png','.jpeg')) and sys.argv[2].endswith(('.jpg','.png','.jpeg')):
        if (sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.jpg')):
            print('jpg')
        elif (sys.argv[1].endswith('.png') and sys.argv[2].endswith('.png')):
            print('.png')
        elif (sys.argv[1].endswith('.jpeg') and sys.argv[2].endswith('.jpeg')):
            print('.jpeg')
        else:
            sys.exit("input and output have different extentions")







if __name__ == '__main__':
    main()
