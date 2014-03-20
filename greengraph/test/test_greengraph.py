from nose.tools import assert_almost_equal
from nose.tools import assert_in, assert_equal, assert_false
from ..greengraph import geolocate, maps_url_for, get_map_at
from ..greengraph import count_green, is_green, location_sequence
import png
import os

def example():
  return png.Reader(filename=(os.path.join(
  os.path.dirname(__file__),"fixtures","london.png"))).asRGB()

def test_geolocate():
  latlong=geolocate("London")
  assert_almost_equal(latlong[0],51.5072,places=2)
  assert_almost_equal(latlong[1], -0.1275,places=2)

def test_generate_url():
  url=maps_url_for(51.5072,-0.1275)
  assert_in("http://maps.googleapis.com/maps/api/staticmap?",url)
  assert_in("center=51.5072,-0.1275",url)
  assert_in("zoom=12",url)
  assert_in("size=400x400",url)
  assert_in("sensor=false",url)

def test_generate_satellite_url():
  url=maps_url_for(51.5072,-0.1275,satellite=True)
  assert_in("maptype=satellite",url)

def test_get_png():
  london=(51.508515, -0.1254872)
  map=get_map_at(*london)
  # Can't compare against fixture because online map changes
  assert_equal(map[3]['size'],(400,400))

def test_count_green():
  assert_equal(count_green(example()),102)

def test_isgreen():
  assert(is_green(10,50,5))
  assert_false(is_green(50,10,5))

def test_locationsequence():
  result=location_sequence((0,0),(10,10),5)
  assert_equal(result[0],(0,0))
  assert_equal(result[1],(2.5,2.5))
