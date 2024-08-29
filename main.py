import requests
from datetime import datetime
import os

WEIGHT = os.getenv('WEIGHT')
HEIGHT = os.getenv('HEIGHT')
AGE = os.getenv('AGE')
USERNAME = os.getenv('USERNAME')
PASS = os.getenv('PASS')

APP_ID = os.getenv('APPID')
API_KEY = os.getenv('APIKEY')

nutrition_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.getenv('SHEETY')

exercise = input("Which exercises did you do: ")

nutrition_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

nutrition_params = {
    'query': exercise,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

response = requests.post(url=nutrition_endpoint, headers=nutrition_headers, json=nutrition_params)
data = response.json()
#print(data)

today = datetime.now().strftime('%d%m%Y')
now = datetime.now().strftime('%X')

for exercise in data['exercises']:
    sheet_input = {
        'workout': {
            'date': today,
            'time': now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint,  
        json=sheet_input,
        auth=(USERNAME, PASS)
    )
