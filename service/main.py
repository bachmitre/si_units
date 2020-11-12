from flask import Flask, request, abort
import json
import os
import conversion
from cache_utils import cache_control, LRUCache

app = Flask(__name__)

# store CACHE_SIZE most recently used request/response in cache
cache = LRUCache(int(os.environ.get('CACHE_SIZE', 10000)))

# conversion rest endpoint
# allow response to be cached by intermediate caches
@app.route("/units/si", methods=['GET'])
@cache_control(hours=24*365)
def convert_units():
    """
    The input is an expression of units as a "units" query parameter
    :return: json response in the form of {"unit_name": <string>, "multiplication_factor": <decimal>}
    """

    # make sure we get a "units" query parameter
    input_units = request.args.get('units') or abort(400)

    # any mal-formatted expression or invalid input unit will result in a 400 error
    try:
        # check if result is in cache
        result = cache.get(input_units)
        if not result:
            units, factor = conversion.to_unit_name_and_factor(input_units)
            result = dict(unit_name=units, multiplication_factor=factor)
            # add result to cache
            cache.put(input_units, result)
    except:
        abort(400)

    return json.dumps(result)


# main function for flask in debug mode (note: this is *not* used when started via gunicorn)
if __name__ == "__main__":
    if os.environ['ENV'] == 'debug':
        app.run(
            host="0.0.0.0",
            port=8000,
            debug=True
        )
