import geopy

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
