class Headers:
    forecast = 'forecast'
    forecast_day = 'forecastday'
    hour = 'hour'
    condition = 'condition'
    text = 'text'
    windspeed = 'wind_mph'
    gust = 'gust_mph'
    temperature = 'temp_c'
    feels_like_temperature = 'feelslike_c'
    time = 'time'


class Endpoints:
    base_url = 'http://api.weatherapi.com/v1/'
    history_route = 'history.json'
    history = f'{base_url}{history_route}'


class Parameters:
    key = 'key'
    location = 'q'
    date = 'dt'
    hour = 'hour'
