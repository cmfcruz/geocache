from flask import jsonify, request, Flask
import controller

app = Flask(__name__)


@app.route("/maps/api/geocode/status")
def status():
    """
    Default response just to check availability.
    """
    # TODO: perform healthchecks
    # - Check database
    # - Check Google API access
    return jsonify({'status': 'online'}), 200


@app.route("/maps/api/geocode/json")
def getjson():
    """
    Passes the request to the method for checking the address in the cache.
    """
    code, result = controller.get_address(request)
    return jsonify(result), code

# # TODO: Support XML output
# @app.route("/maps/api/geocode/xml")
# def getxml():
#     """
#     Passes the request to the method for checking the address in the cache.
#     Formats the response to XML similar to Google's API XML response.
#     """
#     code, result = cache.get_address(request)
#     # TODO: convert JSON result to XML
#     return Response(xml_result, code)
