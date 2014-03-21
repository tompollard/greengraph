import os
from glob import glob
from greengraph import *
from os.path import join,splitext,basename
import csv

locations=open('locations').readlines()

# Make an image file for each location
for location in locations:
  data=get_png_at(*geolocate(location))
  buffer=open(location[:-1]+'.png','w')
  buffer.write(data.read())

# For each image file, turn it into a csv file of pixel triples
for image in glob('*.png'):
  data=open(image)
  rows=read_png(data)
  pix=pixels(rows)
  location=splitext(image)[0]
  buffer=open(location+'.csv','w')
  writer=csv.writer(buffer)
  for pixel in pix:
    writer.writerow(pixel)

# For each csv file, count the green pixels
buffer=open('results','w')
writer=csv.writer(buffer)
for pixelfile in glob('*.csv'):
  data=open(pixelfile)
  reader=csv.reader(data)
  location=splitext(pixelfile)[0]
  count=count_green_pixels(row for row in reader)
  writer.writerow([location,count])
