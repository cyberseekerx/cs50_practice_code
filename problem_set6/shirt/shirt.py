import sys 
from PIL import Image

def main():
    cli_input()
    edit_image()




def cli_input():
    if len(sys.argv) > 3:
        sys.exit(f'too many command-line arguments {len(sys.argv)}')
    elif len(sys.argv) < 3:
        sys.exit(f'too few command-line arguments {len(sys.argv)}')
    elif sys.argv[1].endswith(('.jpg','.png','.jpeg')) and sys.argv[2].endswith(('.jpg','.png','.jpeg')):
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        if (sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.jpg')):
            return input_file , output_file
        elif (sys.argv[1].endswith('.png') and sys.argv[2].endswith('.png')):
            return input_file , output_file
        elif (sys.argv[1].endswith('.jpeg') and sys.argv[2].endswith('.jpeg')):
            return input_file ,output_file
        else:
            sys.exit("input and output have different extentions")


def edit_image():
    shirt = Image.open('shirt.png')
    size = shirt.size
    photo.paste(shirt,shirt)
    print(shirt)
    print(size)








if __name__ == '__main__':
    main()
