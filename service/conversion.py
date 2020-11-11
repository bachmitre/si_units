# coding: utf8
import math
import re
from decimal import Decimal, getcontext

# set decimal precision to 14 significant digits
getcontext().prec = 14

# conversion unit and factor for each valid input
conversion_factors = {
    "minute": {
        "unit": "s",
        "factor": 60,
    },

    "min": {
        "unit": "s",
        "factor": 60,
    },

    "hour": {
        "unit": "s",
        "factor": 3600,
    },

    "h": {
        "unit": "s",
        "factor": 3600,
    },

    "day": {
        "unit": "s",
        "factor": 86400,
    },

    "d": {
        "unit": "s",
        "factor": 86400,
    },

    "degree": {
        "unit": "rad",
        "factor": math.pi / 180,
    },

    "°": {
        "unit": "rad",
        "factor": math.pi / 180,
    },

    "arcminute": {
        "unit": "rad",
        "factor": math.pi / 10800,
    },

    "'": {
        "unit": "rad",
        "factor": math.pi / 10800,
    },

    "arcsecond": {
        "unit": "rad",
        "factor": math.pi / 648000,
    },

    '"': {
        "unit": "rad",
        "factor": math.pi / 648000,
    },

    "hectare": {
        "unit": "m^2",
        "factor": 10000,
    },

    "ha": {
        "unit": "m^2",
        "factor": 10000,
    },

    "litre": {
        "unit": "m^3",
        "factor": 0.001,
    },

    "L": {
        "unit": "m^3",
        "factor": 0.001,
    },

    "tonne": {
        "unit": "kg",
        "factor": 1000,
    },

    "t": {
        "unit": "kg",
        "factor": 1000,
    },

}


# main conversion function
def to_unit_name_and_factor(units):
    """
    Converts expression of valid input units to si units and multiplication factor
    Expression can have parentheses and the operators * and /
    :param units: expression of units
    :return:  tuple of si converted unit name expression and multiplication factor
    """
    # initialize result factor with input
    factor = units

    # get input units as tokens
    tokens = re.split('[()/*]', units)

    # sorting tokens from longest to shortest so we can replace them with si unit and factor
    # (this only works because si factors and input units do not overlap / are prefixes from the other)
    tokens.sort(key=lambda s: len(s), reverse=True)

    # create result units and factor by replacing input units, longest to shortest
    for token in tokens:
        if token:
            units = units.replace(token, conversion_factors.get(token).get('unit'))
            factor = factor.replace(token, "Decimal({})".format(str(conversion_factors.get(token).get('factor'))))

    # evaluate factor expression of decimals and convert to float
    factor = float(eval(factor))

    return units, factor
