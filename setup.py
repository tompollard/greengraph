from setuptools import setup, find_packages
setup(
    name = "GreenGraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],

    install_requires = ['numpy','geopy','pypng'],

    # metadata for upload to PyPI
    author = "James Hetherington",
    author_email = "jamespjh@gmail.com",
    description = "Measure level of greenery from Google Maps",
    license = "MIT",
    keywords = "Environment, geocoding",
    url = "http://development.rc.ucl.ac.uk", # project home page, if any
)
