import validations
from database import Mongo
from apis import Google


def get_address(request):
    """
    This function follows the following process:
    1. Validates if the parameters of the request is valid.
    2. Checks the cache if an existing address is available based on the
       provided latitute & longitude.
    3a. If no address exists in the cache, get the address from Google API.
    3b. Store the result from Google into the cache.
    4. Return the result as response.
    """

    # Validate if request is complete
    valid, code, response = validate_request(request)
    if not valid:
        return code, response

    # Extract parameters from request
    coordinates = request.args.get('latlng').split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    key = request.args.get('key')

    # Check cache for address
    db = Mongo()
    result = db.find_result(latitude, longitude)
    if result:
        return 200, result

    # Check Google API for address
    api = Google()
    result = api.get_result(latitude, longitude, key)
    # Store Google API results into MongoDB
    db.store_result(latitude, longitude, result)
    return 200, result


def validate_request(request):
    # Check if latlng parameter exists
    validity, code, response = validations.check_parameter_existence(
        request, 'latlng')
    if validity is False:
        return validity, code, response

    # Check if latlng can be split into latitude & longitude coordinates
    validity, code, response = validations.check_comma_delimited(
        request, 'latlng')
    if validity is False:
        return validity, code, response

    # Check if latitude & longitude values are valid
    coordinates = request.args.get('latlng').split(',')
    latitude = coordinates[0]
    longitude = coordinates[1]
    validity, code, response = validations.check_non_zero(latitude, 'latlng')
    if validity is False:
        return validity, code, response
    validity, code, response = validations.check_non_zero(longitude, 'latlng')
    if validity is False:
        return validity, code, response

    # Coordinates should be numerical
    # validity, code, response = validations.check_numeric(latitude, 'latlng')
    # if validity is False:
    #     return validity, code, response
    # validity, code, response = validations.check_numeric(longitude, 'latlng')
    # if validity is False:
    #     return validity, code, response

    return True, None, None
