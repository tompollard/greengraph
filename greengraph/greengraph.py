import geopy
import urllib2
import png
from itertools import izip
from numpy import linspace

geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")


def geolocate(place):
    """
    Given a string description of a place, return it's latitude and longitude.
    """
    return geocoder.geocode(place, exactly_one=False)[0][1]


def maps_url_for(lat, long,
                 satellite=False, zoom=12, size=(400, 400), sensor=False):
    url = "http://maps.googleapis.com/maps/api/staticmap?"
    params = dict(
        sensor=str(sensor).lower(),
        zoom=12,
        size="x".join(map(str, size)),
        center=",".join(map(str, (lat, long))),
    )

    if satellite:
        params["maptype"] = "satellite"

    paramstring = "&".join([key + "=" + str(value) for
                            key, value in params.items()])

    return url + paramstring


def get_map_at(lat, long, **args):
    data = urllib2.urlopen(maps_url_for(lat, long, **args))
    return png.Reader(file=data).asRGB()


def count_green(image):
    count = 0
    for row in image[2]:
        pixels = izip(*[iter(row)] * 3)
        # Chunk idiom from http://docs.python.org/2/library/itertools.html#recipes
        # for pixel in pixels:
        # print pixel
        #  if is_green(*pixel):
        #    count+=1
        count += sum(1 for pixel in pixels if is_green(*pixel))
    return count


def is_green(r, g, b):
    return g > r and g > b


def location_sequence(start, end, steps):
    # Would actually prefer this if steps
    # were deduced from zoomlevel
    # But need projection code for that
    lats = linspace(start[0], end[0], steps)
    longs = linspace(start[1], end[1], steps)
    return zip(lats, longs)


def greengraph(start, end, steps, **args):
    locations = location_sequence(geolocate(start), geolocate(end), steps)
    greenness = [
        count_green(get_map_at(lat, long, **args))
        for lat, long in locations]
    return greenness
