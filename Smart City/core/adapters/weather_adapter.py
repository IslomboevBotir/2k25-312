import random
class ExternalWeatherService:
    def get_temp_fahrenheit(self):
        return random.randint(50, 95)
    
    def get_humidity_raw(self):
        return random.random()
    
    def get_condition_code(self):
        """Ob-havo kodini qaytarish"""
        return random.choice([1, 2, 3, 4])


class WeatherAdapter:
    def __init__(self):
        self.external_service = ExternalWeatherService()
        self.condition_map = {
            1: "Ochiq",
            2: "Bulutli",
            3: "Yomg'irli",
            4: "Qorli"
        }
    
    def get_weather_data(self):
        # Fahrenheit dan Celsius ga o'tkazish
        temp_f = self.external_service.get_temp_fahrenheit()
        temp_c = round((temp_f - 32) * 5/9, 1)
        
        # Raw namlikni foizga o'tkazish
        humidity_raw = self.external_service.get_humidity_raw()
        humidity = round(humidity_raw * 100, 1)
        
        # Kod nomini olish
        code = self.external_service.get_condition_code()
        conditions = self.condition_map.get(code, "Noma'lum")
        
        return {
            'temperature': temp_c,
            'humidity': humidity,
            'conditions': conditions
        }