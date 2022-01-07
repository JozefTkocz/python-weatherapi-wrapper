import datetime as dt
from typing import Union

import pandas as pd

from api.interface import APICaller
from helpers import generate_date_range_for_period
from api.parser import extract_hourly_timeseries_frame


def get_weather_history(api_key: str, latitude: float, longitude: float, start_time: dt.datetime,
                        end_time: Union[dt.datetime, None] = None) -> pd.DataFrame:
    api_caller = APICaller(api_key)
    date_range = generate_date_range_for_period(start_time, end_time)

    history = pd.DataFrame()
    for date in date_range:
        response_json = api_caller.get_history(latitude, longitude, date, hour=None)
        data = extract_hourly_timeseries_frame(response_json)
        history = history.append(data)

    return history