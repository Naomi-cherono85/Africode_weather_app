import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


api_key = os.getenv('API_KEY')

def get_coordinates(city_name, country_code):
    response = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}"
    data = requests.get(response).json()
    if data:
        latitude = data[0].get('lat')
        longitude = data[0].get('lon')
        return latitude, longitude
    else:
        return None, None    


def get_weather(latitude,longitude,api_key):
    response = requests.post(f"{BASE_URL}",params={'lat':latitude,'lon':longitude,'appid':api_key,'units':'metric'})
    data = response.json()
    if data:
        precipitation = data['weather'][0]['main']
        prec_description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        timezone_offset = data["timezone"]
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timestamp = data['dt']
        sunrise_time = datetime.fromtimestamp(sunrise) + timedelta(seconds=timezone_offset)
        sunset_time = datetime.fromtimestamp(sunset) + timedelta(seconds=timezone_offset)
        formatted_sunrise = sunrise_time.strftime("%I:%M %p")  
        formatted_sunset = sunset_time.strftime("%I:%M %p") 
        utc_time = datetime.fromtimestamp(timestamp,tz=timezone.utc)
        local_time = utc_time + timedelta(seconds=timezone_offset)
        date = local_time.strftime("%A, %-d %B %Y") 
        day = local_time.day
        if 11 <= day <= 13:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        formatted_date = local_time.strftime(f"%A, {day}{suffix} %B %Y")



        data = {
            'precipitation': precipitation,
            'prec_description': prec_description,
            'icon': icon,
            'temp': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
           'sunrise': formatted_sunrise,
           'sunset': formatted_sunset,
            'date': formatted_date,
        }
        return data
    else:
        return None
    
def get_requested_weather(city, country):
    latitude, longitude = get_coordinates(city, country)
    if latitude and longitude:
        return get_weather(latitude, longitude, api_key)
    else:
        return None
