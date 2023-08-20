import sys
import os
from PIL import Image
import math

list = ['Test1.jpg', 'Test1.jpg']
#get list of all images in folder current folder
list = os.listdir(os.getcwd())
images = []
#remove all non jpg files
for i in list:
    if i.endswith('.png'):
        if ( i != 'SpriteSheet.png'):
          images.append(i)


#get the size of the first image
img = Image.open(images[0])
width, height = img.size

#calculate the size of the sprite sheet
# make it a square, other wise add and extra row

squareRt = math.sqrt(len(images))
dim = int(squareRt)
extraRow = 0 
if squareRt - dim > 0.5:
    dim += 1
else: 
  if (dim < squareRt):
      extraRow = 1
sheetWidth = width * dim
sheetHeight = height * (dim + extraRow)

  

#create the sprite sheet
spriteSheet = Image.new('RGBA', (int(sheetWidth), int(sheetHeight)))

#paste the images into the sprite sheet
x = 0
y = 0
for i in images:
    img = Image.open(i)
    spriteSheet.paste(img, (x, y))
    x += width
    if x >= sheetWidth:
        x = 0
        y += height

#save the sprite sheet
spriteSheet.save('SpriteSheet.png')