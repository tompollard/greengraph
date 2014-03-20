from nose.tools import assert_almost_equal
from ..greengraph import geolocate

def test_geolocate():
  latlong=geolocate("London")
  assert_almost_equal(latlong[0],51.5072,places=2)
  assert_almost_equal(latlong[1], -0.1275,places=2)
