import datetime as dt
from typing import Union

import requests

from weatherapi.api.constants import Parameters, Endpoints


class APINotCalledException(Exception):
    pass


class APICaller:
    def __init__(self, api_key):
        self.key = api_key

    def get_history(self, latitude: float, longitude: float, day: dt.date, hour: Union[int, None]) -> dict:
        request_parameters = self._build_parameters_dict(latitude=latitude,
                                                         longitude=longitude,
                                                         day=day,
                                                         hour=hour)

        response = requests.get(Endpoints.history, params=request_parameters)
        if not response.status_code == 200:
            raise APINotCalledException(response.text)

        return response.json()

    def _build_parameters_dict(self, latitude, longitude, day, hour=None) -> dict:
        parameters = {Parameters.key: self.key,
                      Parameters.location: f'{latitude},{longitude}',
                      Parameters.date: day}
        if hour is not None:
            parameters.update({Parameters.hour: hour})

        return parameters
