import datetime as dt
import json
import os
from unittest.mock import patch

import pandas as pd

from weatherapi import get_weather_history
from weatherapi.web_api.interface import APICaller

TEST_FOLDER = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(TEST_FOLDER, 'data')

ANY_FLOAT = 0.01
ANY_INT = 2

example_json_data_filepath = os.path.join(DATA_FOLDER, 'example.json')

with open(example_json_data_filepath, 'r') as file:
    example_data = json.load(file)


@patch.object(APICaller, "get_history")
def test_get_weather_history_returns_dataframe(get_history):
    get_history.return_value = example_data
    result = get_weather_history(api_key='A_STRING', latitude=ANY_FLOAT, longitude=ANY_FLOAT,
                                 start_time=dt.datetime(year=2022, month=1, day=7),
                                 end_time=None)
    assert type(result) == pd.DataFrame


@patch.object(APICaller, "get_history")
def test_get_weather_history_appends_subsequent_calls(get_history):
    get_history.return_value = example_data

    # make a call that spans two days
    result = get_weather_history(api_key='A_STRING', latitude=ANY_FLOAT, longitude=ANY_FLOAT,
                                 start_time=dt.datetime(year=2022, month=1, day=7),
                                 end_time=dt.datetime(year=2022, month=1, day=8))

    # expect 48 entries in returned dataframe (2 * 24 1hr periods).
    assert len(result) == 48
