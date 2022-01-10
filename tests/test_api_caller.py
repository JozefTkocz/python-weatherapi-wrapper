import datetime as dt
from unittest.mock import Mock

import requests

from weatherapi.web_api.interface import APICaller


def test_build_parameters_dict():
    caller = APICaller('ANY_STRING')
    actual_result = caller._build_parameters_dict(latitude=12, longitude=34, day=dt.datetime(year=2022,
                                                                                             month=1,
                                                                                             day=1), hour=None)

    expected_result = {'key': 'ANY_STRING',
                       'q': '12,34',
                       'dt': '2022-01-01'}

    assert actual_result == expected_result


def test_build_parameters_dict_with_hour_argument():
    caller = APICaller('ANY_STRING')
    actual_result = caller._build_parameters_dict(latitude=12, longitude=34, day=dt.datetime(year=2022,
                                                                                             month=1,
                                                                                             day=1), hour=5)

    expected_result = {'key': 'ANY_STRING',
                       'q': '12,34',
                       'dt': '2022-01-01',
                       'hour': 5}

    assert actual_result == expected_result
