import datetime as dt

import pandas as pd
import pytest
from pandas.testing import assert_index_equal

from weatherapi.helpers import generate_date_range_for_period


def test_generate_date_range_for_period_multiple_days_with_datetimes():
    start_date = dt.datetime(year=2022, month=1, day=1, hour=12)
    end_date = dt.datetime(year=2022, month=1, day=2, hour=5)

    expected_result = pd.DatetimeIndex([pd.Timestamp(start_date).date(), pd.Timestamp(end_date).date()], freq='D')
    actual_result = generate_date_range_for_period(start_date, end_date)

    assert_index_equal(expected_result, actual_result)


def test_generate_date_range_for_period_multiple_days_with_dates():
    start_date = dt.datetime(year=2022, month=1, day=1)
    end_date = dt.datetime(year=2022, month=1, day=2)

    expected_result = pd.DatetimeIndex([pd.Timestamp(start_date).date(), pd.Timestamp(end_date).date()], freq='D')
    actual_result = generate_date_range_for_period(start_date, end_date)

    assert_index_equal(expected_result, actual_result)


def test_generate_date_range_for_period_only_start_datetime():
    start_date = dt.datetime(year=2022, month=1, day=1, hour=12)
    end_date = None

    expected_result = pd.DatetimeIndex([pd.Timestamp(start_date).date()], freq='D')
    actual_result = generate_date_range_for_period(start_date, end_date)

    assert_index_equal(expected_result, actual_result)


def test_generate_date_range_for_period_only_start_date():
    # only date, no clock time information
    start_date = dt.datetime(year=2022, month=1, day=1)
    end_date = None

    expected_result = pd.DatetimeIndex([pd.Timestamp(start_date).date()], freq='D')
    actual_result = generate_date_range_for_period(start_date, end_date)

    assert_index_equal(expected_result, actual_result)


def test_generate_date_range_for_period_start_and_end_are_same_day():
    start_date = dt.datetime(year=2022, month=1, day=1, hour=10)
    end_date = dt.datetime(year=2022, month=1, day=1, hour=15)

    # result should be a daterange index containing two dates
    expected_result = pd.DatetimeIndex([pd.Timestamp(start_date).date()], freq='D')
    actual_result = generate_date_range_for_period(start_date, end_date)

    assert_index_equal(expected_result, actual_result)


def test_generate_date_range_for_period_raises_exception_if_end_before_start():
    start_date = dt.datetime(year=2022, month=1, day=2, hour=12)
    end_date = dt.datetime(year=2022, month=1, day=1, hour=12)

    with pytest.raises(Exception) as e_info:
        generate_date_range_for_period(start_date, end_date)
