import telebot
from get_city import get_city_id_by_name
from get_city import city_checker
from api_tokens import telegram_my_weather_bot_token
from weather_getter import Weather



bot = telebot.TeleBot(telegram_my_weather_bot_token)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard1.add('Simferopol', 'Kyiv', 'Kharkiv', 'Odesa', 'Dnipro', 'Lviv', 'Poltava', 'Ternopil', 'Sumy')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hey, I can show you weather in some cities! Please choose one or type any ',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_weather_overall(message):
    city_name = message.text
    if city_checker(city_name=city_name) == "OK":
        weather_in_requested_city = Weather(get_city_id_by_name(city_name=city_name))
        weather_parsed_to_be_sent = weather_in_requested_city.clouds_weather_info_data_parser(
            weather_in_requested_city.request_to_open_weather_api())
        temp_parsed_to_be_sent = weather_in_requested_city.get_and_convert_temperature(
            weather_in_requested_city.request_to_open_weather_api())
        bot.send_message(message.chat.id, f"In {city_name} it's {temp_parsed_to_be_sent} degrees, "
                                          f"{weather_parsed_to_be_sent}")
    else:
        bot.send_message(message.chat.id, "no such city")


bot.polling()
