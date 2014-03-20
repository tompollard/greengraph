from nose.tools import assert_almost_equal, assert_in
from ..greengraph import geolocate, maps_url_for

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
