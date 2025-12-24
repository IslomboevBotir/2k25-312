class ExternalWeatherService:
    # Simulated 3rd-party API
    def get_forecast_json(self):
        return {'temp_c': 22, 'condition': 'clear', 'wind_kph': 10}

class WeatherAdapter:
    def __init__(self):
        self._service = ExternalWeatherService()

    def get_temperature_celsius(self):
        data = self._service.get_forecast_json()
        return data['temp_c']

    def is_rain_expected(self):
        data = self._service.get_forecast_json()
        return 'rain' in data['condition'].lower()
