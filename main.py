import requests
import datetime
import os

today = datetime.datetime.now().date().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")

API_ID = os.environ.get('API_ID')
API_KEY = os.environ['API_KEY']


HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Authorization": os.environ["HEADERS_AUTH"]
}

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_GET = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/workoutTrackking/workouts"
SHEETY_POST = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/workoutTrackking/workouts"

exercise_config = {
    "query":input("What did you do?: "),
    "gender":"male",
    "weight_kg":70.0,
    "height_cm":188.0,
    "age":25,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_config, headers=HEADERS)
result = response.json()
exercise = result['exercises'][0]['name'].title()
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

sheety_parameters = {
    "workout":{
        "date": today,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

response_sheet = requests.post(SHEETY_POST, json=sheety_parameters, headers=HEADERS)
