import json
import os

import pandas as pd
from pandas.testing import assert_index_equal

from weatherapi.web_api.parser import extract_hourly_timeseries_frame

TEST_FOLDER = os.path.dirname(__file__)
DATA_FOLDER = os.path.join(TEST_FOLDER, 'data')

example_json_data_filepath = os.path.join(DATA_FOLDER, 'example.json')

with open(example_json_data_filepath, 'r') as file:
    example_data = json.load(file)


def test_extract_hourly_timeseries_frame_returns_dataframe():
    actual_result = extract_hourly_timeseries_frame(example_data)

    assert type(actual_result) is pd.DataFrame


def test_extract_hourly_timeseries_frame_has_expected_columns():
    # do not expect to see time column, as this should be set as the index of the returned dataframe
    expected_columns = ["time_epoch", "temp_c", "temp_f", "is_day", "condition", "wind_mph", "wind_kph", "wind_degree",
                        "wind_dir", "pressure_mb", "pressure_in", "precip_mm", "precip_in", "humidity", "cloud",
                        "feelslike_c", "feelslike_f", "windchill_c", "windchill_f", "heatindex_c", "heatindex_f",
                        "dewpoint_c", "dewpoint_f", "will_it_rain", "chance_of_rain", "will_it_snow", "chance_of_snow",
                        "vis_km", "vis_miles", "gust_mph", "gust_kph"]

    data = extract_hourly_timeseries_frame(example_data)
    assert list(data.columns.values) == expected_columns


def test_extract_hourly_timeseries_frame_has_time_correct_index():
    data = extract_hourly_timeseries_frame(example_data)

    expected_index = pd.date_range("2022-01-07 00:00", "2022-01-07 23:00", freq='1H')
    expected_index.name = 'time'
    actual_index = data.index
    assert_index_equal(actual_index, expected_index)
