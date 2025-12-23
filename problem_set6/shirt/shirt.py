import sys 
from PIL import Image, ImageOps

##only two input accepted 


if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

input = sys.argv[1]
output = sys.argv[2]

try:
    file_input,input_extention = input.split('.')

    file_output,output_extention = output.split('.')
except:
   sys.exit('invalid input')
#check if the file are .jpg ,png ,jpeg 


extentions = input_extention == output_extention
if  input_extention and output_extention not in ('jpg','png','jpeg') :
    sys.exit('invalid input')
if not extentions :
    sys.exit('Input and output have different extensions')
try:
    #input size  1200 x 1600
    input = Image.open(input)
    shirt = Image.open('shirt.png')
    size = shirt.size
    input = ImageOps.fit(input,size) 
    ##crop and resize the shirt.png
    shirt = ImageOps.fit(shirt,size,method=0 ,bleed =(0.0),centering = (0.5,0.5))
    input.paste(shirt,(0,0),mask = shirt)
    input.save(output)
    


    
except FileNotFoundError:
    sys.exit('Input does not exit')



    
