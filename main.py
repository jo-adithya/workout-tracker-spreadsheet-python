from dotenv import load_dotenv
import requests
import os
load_dotenv()

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
print(response.json())




