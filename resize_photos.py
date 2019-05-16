from PIL import Image
import os


basewidth = 256
height = 256
i=0
for filename in os.listdir('.'):
    if filename.endswith(".jpg"): 
        img = Image.open(filename)
        img = img.resize((basewidth, height), Image.ANTIALIAS)
        i+=1
        print(i, filename)
        img.save(filename)


