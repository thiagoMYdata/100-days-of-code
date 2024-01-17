import datetime as dt
import requests

from tkinter import *
from tkinter import messagebox


APP_ID = # user_id
APP_KEY = #user key
SHEETY_TOKEN = # token


exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-key' : APP_KEY,
    'x-app-id' : APP_ID
}
query = {
    'query' : 'today i jump rope for about 24 minutes'
}


response = requests.post(url=exercise_endpoint, json=query, headers=headers)
response = response.json()['exercises']

# print(response)

new_key = ['exercise', 'duration', 'calories']


for j in range(len(response)):
    clean_result = {key : response[j][key] for key in dict(response[j]).keys() if key in  ['user_input','duration_min','nf_calories'] }
    data_to_sheets = {'workout':{}}
    for index, value in enumerate(['user_input','duration_min','nf_calories']):
        data_to_sheets['workout'][new_key[index]] = clean_result[value]


    # print(data_to_sheets)
    # clean_result = {new_key[index] : clean_result[old_key] for old_key in ['user_input','duration_min','nf_calories']}
    today = dt.datetime.now()

    data_to_sheets['workout']['date'] = today.strftime('%d/%m/%Y')
    data_to_sheets['workout']['time'] = today.strftime('%X')

    # print(data_to_sheets)


    sheety_endpoint = # endpoint



    response_sheets = requests.post(url=sheety_endpoint, json=data_to_sheets, headers={'Authorization' : SHEETY_TOKEN})

    print(response_sheets.text)

