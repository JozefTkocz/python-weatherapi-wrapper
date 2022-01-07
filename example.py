import os
import datetime as dt
from endpoint_methods import get_weather_history

API_KEY = '2465dde64d724086a37103530220701'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    latitude = 56.19063
    longitude = -4.63317
    start_time = dt.datetime.now() - dt.timedelta(days=3)
    end_time = dt.datetime.now() - dt.timedelta(days=1)

    df = get_weather_history(API_KEY, latitude, longitude, start_time=start_time, end_time=end_time)

    print(df)