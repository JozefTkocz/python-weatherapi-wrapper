import datetime as dt
from typing import Union

import pandas as pd


def generate_date_range_for_period(start_time: dt.datetime, end_time: Union[dt.datetime, None]) -> pd.DatetimeIndex:
    if end_time is None:
        end_time = start_time

    assert start_time <= end_time, 'start date must be before end date.'

    start_date = start_time.date()
    end_date = end_time.date()

    date_range = pd.date_range(start=start_date, end=end_date, freq='1D')
    return date_range
