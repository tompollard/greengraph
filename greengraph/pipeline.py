import os
from glob import glob
from greengraph import *
from os.path import join,splitext,basename
import csv

locations=open('locations').readlines()

# Make an image file for each location
for location in locations:
  data=get_png_at(*geolocate(location))
  buffer=open(join('images',location[:-1])+'.png','w')
  buffer.write(data.read())

# For each image file, turn it into a csv file of pixel triples
for image in glob('images/*.png'):
  data=open(image)
  rows=read_png(data)
  pix=pixels(rows)
  location=splitext(basename(image))[0]
  buffer=open(join('pixelfiles',location)+'.csv','w')
  writer=csv.writer(buffer)
  for pixel in pix:
    writer.writerow(pixel)

# For each csv file, count the green pixels
buffer=open('results.csv','w')
writer=csv.writer(buffer)
for pixelfile in glob('pixelfiles/*.csv'):
  data=open(pixelfile)
  reader=csv.reader(data)
  location=splitext(basename(pixelfile))[0]
  count=count_green_pixels(row for row in reader)
  writer.writerow([location,count])
