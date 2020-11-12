from flask import Flask, request, abort
import json
import os
import conversion
from cache_utils import cache_control

app = Flask(__name__)

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
        units, factor = conversion.to_unit_name_and_factor(input_units)
    except Exception as e:
        app.logger.error("Error converting {}: {}".format(input_units, e))
        abort(400)

    return json.dumps(dict(unit_name=units, multiplication_factor=factor))


# main function for flask in debug mode (note: this is *not* used when started via gunicorn)
if __name__ == "__main__":
    if os.environ['ENV'] == 'debug':
        app.run(
            host="0.0.0.0",
            port=8000,
            debug=True
        )
