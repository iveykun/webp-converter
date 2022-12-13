from PIL import Image
import os
import glob
import datetime
counter=924
savelocation = os.getcwd()
x = datetime.datetime.now()
# for every item in this folder that ends with .webp
for item in glob.iglob(savelocation + r'/*.webp'):
    print("Original:")
    #print(item)
    #open and convert to RGB
    im = Image.open(item).convert("RGB")
    # new unique name for the picture
    name = savelocation + '/' + x.strftime("%f")+str(counter) + ".png"
    counter = counter+1
    #print("New:")
    print(name)
    im.save(name,"png")
    #delete the original webp
    #os.remove(item)
    print("--------")
