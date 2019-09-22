import requests
import pytemperature
from api_tokens import open_weather_api_token


class Weather:

    def __init__(self, city_id, open_weather_token=open_weather_api_token, weather_info={}):
        self.city_id = city_id
        self.open_weather_token = open_weather_token
        self.weather_info = weather_info

    def request_to_open_weather_api(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?id={self.city_id}&APPID={self.open_weather_token}"
        response_from_open_weather = requests.get(url=url)
        self.weather_info = response_from_open_weather.json()
        return self.weather_info

    def clouds_weather_info_data_parser(self, weather_info):
        weather_list = weather_info['weather']
        weather_dict = weather_list[0]
        weather_in_the_sky_to_user = weather_dict['description']
        return weather_in_the_sky_to_user

    def get_and_convert_temperature(self, weather_info):
        weather_main = weather_info['main']
        temp_kelvin = weather_main['temp']
        temp = int(pytemperature.k2c(temp_kelvin))
        return temp
