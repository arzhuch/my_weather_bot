# MyWeatherBot

This is Telegram bot (in Python) who can show you current weather in ~5000 cities per\
your request

Bot:
* receives text message (name of city) from user
* goes to file to check if we have such city
* gets city id by name given by user
* sends GET request to weather service to retrieve weather by city id
* parses retrieved data to json
* extracts sky status and temperature, converts it from Kelvin to Celsius
* parses this data into single string and returns it to user

## Getting Started

To talk to bot, simply follow the link: https://t.me/artem_weather_bot

## What in there

1. bot itself - talks to you (bot.py)
2. city database (city.list.json)
3. cities module (check if city name is in database, get city id by city name)
4. weather module (weather_getter.py) - sends requests to OpenWeatherMap API
5. file with API tokens (api_tokens.py)
6. automated tests (tests.py)

### Prerequisites

No special equipment or skills needed (except for small geography:)

```
Remember - Kyiv not Kiev!
```

Tap 'Start' button. You'll be prompted to select one of the Ukrainian cities to\
check weather - or you can type your own. We have more than 5000 cities in\
our database, so most probably you city is there!

## Running the tests

install and import requests module. run tests.py module. No arguments required.

## Built With

* [OpenWeatherMap](https://openweathermap.org/api) - The weather provider
* [Telegram Api](https://telegram.me/BotFather) - Your favorite messenger
* Big Love 

## Authors

* [Artem Zhuchenko](https://t.me/@artem_zhuchenko)

## Acknowledgments

* @Yurii_Khomych
* @ITEA
