from dotenv import load_dotenv
import requests
from datetime import datetime
import os
load_dotenv()

# NUTRITIONIX
GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 17

API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
APP_ID = os.environ.get('NUTRITIONIX_APPID')

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

query = input('Tell me which exercise you did: ')

parameters = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=url, headers=headers, json=parameters)
exercises = response.json()['exercises']

# SHEETY
USERNAME = os.environ.get('SHEETY_USERNAME')
PROJECT_NAME = os.environ.get('SHEETY_PROJECT_NAME')
SHEET_NAME = os.environ.get('SHEETY_SHEET_NAME')
BEARER = os.environ.get('BEARER')

sheety_headers = {
    'Authorization': f'Bearer {BEARER}',
    'Content-Type': 'application/json'
}

date = datetime.now()
sheety_url = f'https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}'

for exercise in exercises:
    row_body = {
        'workout': {
            'date': date.strftime('%d/%m/%Y'),
            'time': date.strftime('%-I:%M:%S %p'),
            'exercise': exercise['name'].title(),
            'duration': int(str(exercise['duration_min'])),
            'calories': exercise['nf_calories']
        }
    }
    sheet_response = requests.post(url=sheety_url, json=row_body, headers=sheety_headers)





