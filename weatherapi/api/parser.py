import pandas as pd

from weatherapi.api.constants import Headers


def extract_hourly_timeseries_frame(history_result: dict) -> pd.DataFrame:
    hourly_weather = history_result.get(Headers.forecast).get(Headers.forecast_day)[0].get(Headers.hour)

    result = pd.DataFrame()

    for item in hourly_weather:
        result = result.append(item, ignore_index=True)

    result[Headers.time] = pd.to_datetime(result[Headers.time])

    return result.set_index(Headers.time).sort_index()