import requests

endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
api_key = 'f73667bd77b3c03230311cb6d6bc0dd8'


# parameters = {'lat' : -23.960795, 'lon' : -46.376799, 'appid' : api_key, 'cnt' : 4}

parameters = {'lat' : 32.46794832067919, 'lon' : -84.98606118498479, 'appid' : api_key, 'cnt' : 4}

response = requests.get(url=endpoint, params=parameters)

response.raise_for_status()

# print(response.status_code)

response = response.json()['list']

code_weather = []


for iten in response:
    code_weather.append( iten['weather'][0]['id'])


if any(code_weather) < 800:
    print('Dont forget to bring ur umbrella')
else:
    print('dont need to worry about the weather today')
