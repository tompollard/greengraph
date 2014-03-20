from nose.tools import assert_almost_equal
from nose.tools import assert_in, assert_equal
from ..greengraph import geolocate, maps_url_for, get_map_at
import png
import os

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
  example=png.Reader(filename=(os.path.join(
    os.path.dirname(__file__),"fixtures","london.png"))).asRGB()[2]
  for a,b in zip(example,map[2]):
    assert_equal(a,b)
