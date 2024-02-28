import os
import dotenv

import aiohttp.client
from aiogram.types import Location

dotenv.load_dotenv()

WEATHER_SERVICE_API_KEY = os.getenv('WEATHER_SERVICE_API_KEY')

class WeatherServiceException(BaseException):
    pass


class WeatherInfo:

    def __init__(self, temperature, status, is_kelvin=True):
        self.temperature = kelvin_to_celsius(
            temperature) if is_kelvin else temperature
        self.status = status


async def get_weather_for_city(city_name: str) -> WeatherInfo:
    loc = await city_to_location(city_name)
    return await get_weather_for_location(loc)


async def get_weather_for_location(location: Location) -> WeatherInfo:
    return await make_weather_service_query(get_location_query_url(location))


async def city_to_location(city_name: str) -> Location:
    url_for_city = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={WEATHER_SERVICE_API_KEY}&lang=ru&limit=1'
    async with aiohttp.ClientSession() as session:
        async with session.get(url_for_city) as responce:
            if(responce.status != 200): return
            json = await responce.json()
            json = json[0]
            loc = Location()
            loc.latitude = json['lat']
            loc.longitude = json['lon']
            return loc


def get_location_query_url(location: Location):
    return f'http://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&appid={WEATHER_SERVICE_API_KEY}&lang=ru'


async def make_weather_service_query(url: str) -> WeatherInfo:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return get_weather_from_response(await resp.json())

    raise WeatherServiceException()


def get_weather_from_response(json):
    json = json['list'][0]
    return WeatherInfo(json['main']['temp'], json['weather'][0]['description'])


def kelvin_to_celsius(degrees):
    KELVIN_0 = 273.15
    return degrees - KELVIN_0
