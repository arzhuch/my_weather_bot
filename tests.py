from get_city import get_city_id_by_name
from get_city import city_checker
from weather_getter import Weather

city_name = "Kyiv"
weather_in_city = Weather(get_city_id_by_name(city_name=city_name))

assert (isinstance(weather_in_city, Weather)) is True, "should be object of Weather class"

assert city_checker("Kyiv") is "OK", "should be OK"

assert isinstance(get_city_id_by_name("Lviv"), int) is True, "should be integer"

assert city_checker("Kiev") is not "OK", "should be not OK"


weather_in_city.request_to_open_weather_api()
weather_parsed_to_be_sent = weather_in_city.clouds_weather_info_data_parser(
            weather_in_city.request_to_open_weather_api())

assert isinstance(weather_parsed_to_be_sent, str)
