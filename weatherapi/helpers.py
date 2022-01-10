import datetime as dt

import pandas as pd

from typing import Union


def generate_date_range_for_period(start_time: dt.datetime, end_time: Union[dt.datetime, None]) -> pd.DatetimeIndex:
    if end_time is None:
        end_time = start_time

    assert start_time <= end_time, 'start date must be before end date.'

    start_date = pd.Timestamp(start_time).floor('1D')
    end_date = pd.Timestamp(end_time).ceil('1D') - pd.to_timedelta('1D')

    date_range = pd.date_range(start=start_date, end=end_date, freq='1D')
    return date_range