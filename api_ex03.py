import requests as req
import json
from api_ex02 import download

API_KEY = '73594ac2d49706895467644d288b2f19'

def get_weather(city='Seoul'):
  URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&lang=kr&units=metric'
  print(URL)
  weather = {}
  res = req.get(URL)
  if res.status_code == 200:
    result = res.json()
    print(type(res))
    weather['main'] = result['weather'][0]['main']
    weather['description'] = result['weather'][0]['description']
    print(result['weather'][0]['description'])
    icon = result['weather'][0]['icon']
    weather['icon'] = f'http://openweathermap.org/img/w/{icon}.png'
    weather['etx'] = result['main']
    # download(weather['icon'],weather['icon'].split('/')[-1])
  else:
    print('error', res.status_code)
  return weather
weather = get_weather()
print(json.dumps(weather, indent=4, ensure_ascii=False))