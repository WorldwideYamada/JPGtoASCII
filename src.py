from PIL import Image
import os.path

try:
    img = Image.open("miku.jpg").rotate(90) #Edit image name to your own image
    f = open("ascii.txt", "w") #Creates new file to write ASCII art to


except FileNotFoundError:
    f = open("ascii.txt", "w")
    f.write("Image not found/File Type not supported")



for x in range(0, img.size[0]):
    for y in range(0, img.size[1])[::-1]:

        #Convert pixel at current coordinate to grayscale
        coordinate = (x, y)
        grayscale = round((img.getpixel(coordinate)[0] + img.getpixel(coordinate)[1] + img.getpixel(coordinate)[2])/3)
        img.putpixel(coordinate,(grayscale, grayscale, grayscale))

        #Write ASCII character based on grayscale value
        if img.getpixel(coordinate)[0] > 175:
            f.write("@")
        elif img.getpixel(coordinate)[0] > 125:
            f.write("O")
        elif img.getpixel(coordinate)[0] > 75:
            f.write("/")
        else:
            f.write(" ")
    
    f.write("\n")