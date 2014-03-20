import geopy
import urllib2
import png
from itertools import izip

geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

def geolocate(place):
  """
  Given a string description of a place, return it's latitude and longitude.
  """
  return geocoder.geocode(place)[1]

def maps_url_for(lat,long,
  satellite=False,zoom=12,size=(400,400),sensor=False):
  url="http://maps.googleapis.com/maps/api/staticmap?"
  params=dict(
    sensor= str(sensor).lower(),
    zoom= 12,
    size= "x".join(map(str,size)),
    center= ",".join(map(str,(lat,long))),
  )

  if satellite:
    params["maptype"]="satellite"

  paramstring="&".join([key+"="+str(value) for
    key,value in params.items()])

  return url+paramstring

def get_map_at(lat,long,**args):
  data=urllib2.urlopen(maps_url_for(lat,long,**args))
  return png.Reader(file=data).asRGB()

def count_green(image):
  count = 0
  for row in image[2]:
    pixels=izip(*[iter(row)]*3)
    # Chunk idiom from http://docs.python.org/2/library/itertools.html#recipes
    count+=sum(1 for pixel in pixels if is_green(*pixel))
  return count

def is_green(r,g,b):
  return g>(r+b)
