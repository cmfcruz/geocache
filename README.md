# Address Cache Using MongoDB

## Introduction

Acts as a drop-in cache for Google API Reverse Geocoder responses to locations.  Allows you to use addresses of "near" locations based on a specified maximum distance if tolerable.  The cache is good for edge cases when most location requests are centered around certain "hot spots" and the addresses are only used to validate if the location is near a specific place of interest.

## TODO
- Drop-in request transparency.  Same format as Google API
- Exception handlers
- Unit tests
- Proper logger
- Unit testing
- XML Output Support

## References
- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro#GeocodingRequests)
- [JSend format used for error messages.](https://github.com/omniti-labs/jsend)
- [Squash irrelevant commits in your feature branches for a cleaner git history.](https://github.com/wprig/wprig/wiki/How-to-squash-commits)