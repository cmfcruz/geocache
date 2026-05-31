# Address Cache Using MongoDB

## Introduction

Acts as a drop-in cache for Google API Reverse Geocoder responses to locations.  Allows you to use addresses of "near" locations based on a specified maximum distance if tolerable.  The cache is good for edge cases when most location requests are centered around certain "hot spots" and the addresses are only used to validate if the location is near a specific place of interest.

## Quick Start Guide
Run a MongoDB local database using Docker:
```bash
docker run --name mongo -d mongo:latest
```


Run the Address Cache app using Gunicorn:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn app:app
```


Make sure that the app is accessible by doing a GET HTTP request to the local URL:

http://localhost:8000/maps/api/geocode/status


Try retrieving a location by doing a GET HTTP request with valid coordinates and a Google API key. See the sample request below:

https://localhost:8000/maps/api/geocode/json?latlng=14.4288586,121.0229493&key=MkVEREI1MkItQUEyRS00Qzg0LThCRTAtQjE1N0IwRDFDMkM4Cg


## TODO
- Exception handlers
- Unit tests
- Proper logger
- Unit testing
- XML Output Support

## References
- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro#GeocodingRequests)
- [JSend format used for error messages.](https://github.com/omniti-labs/jsend)
- [Squash irrelevant commits in your feature branches for a cleaner git history.](https://github.com/wprig/wprig/wiki/How-to-squash-commits)
