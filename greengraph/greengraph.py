import geopy

geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

def geolocate(place):
  """
  Given a string description of a place, return it's latitude and longitude.
  """
  return geocoder.geocode(place)[1]
