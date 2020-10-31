# coding: utf8
import service.main


def test_conversion():

    # multiple test cases, invalid input will result in an exception

    test_cases = {

        '(degree/minute)': {
            "unit_name": "(rad/s)",
            "multiplication_factor": .00029088820866572
        },

        '(degree/min)': {
            "unit_name": "(rad/s)",
            "multiplication_factor": .00029088820866572
        },

        '(°/min)': {
            "unit_name": "(rad/s)",
            "multiplication_factor": .00029088820866572
        },

        '(degree/(minute*hectare))': {
            "unit_name": "(rad/(s*m^2))",
            "multiplication_factor": 2.9088820866572e-08
        },

        # empty input
        '': {
            "unit_name": None,
            "multiplication_factor": None
        },

        # not matching parentheses
        '((degree/(minute*hectare))': {
            "unit_name": None,
            "multiplication_factor": None
        },

        # invalid unit name
        '(degreee/(minute*hectare))': {
            "unit_name": None,
            "multiplication_factor": None
        },

        # invalid operator
        '(degree/(minute+hectare))': {
            "unit_name": None,
            "multiplication_factor": None
        },

    }

    for k, v in test_cases.items():
        unit_name, multiplication_factor = None, None
        try:
            unit_name, multiplication_factor = service.main.to_unit_name_and_factor(k)
        except:
            pass
        finally:
            assert unit_name == v['unit_name']
            assert multiplication_factor == v['multiplication_factor']
