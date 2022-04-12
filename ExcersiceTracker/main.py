import requests
import datetime as dt

#------------------------ nutrition API details -----------------------------#
AUTH_KEY = "f57fa4005f2137263b3d478b26f5b2ba"
APP_ID = "7624e53f"
url = "https://trackapi.nutritionix.com"

#------------------------- sheety API details -------------------------------#
sheety_url = "https://api.sheety.co"



excercise_endpoint = f"{url}/v2/natural/exercise"

req_headers = {
    "x-app-id": APP_ID,
    "x-app-key": AUTH_KEY,
    "Content-Type": "application/json"
}

req_body = {
 "query":input("Tell me which excersices you did today?: "),
 "gender":"female",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
}

resp = requests.post(url=excercise_endpoint, json=req_body, headers=req_headers)
resp.raise_for_status()
workout_data = resp.json()
duration_min = workout_data["exercises"][0]["duration_min"]
calories_burned = workout_data["exercises"][0]["nf_calories"]
excersice_type = workout_data["exercises"][0]["name"]

#-------------- sheety workings --------------------------------------------#
sheety_endpoint = "/4166d676b55b21c519cd0267e9889bf2/exerciseTracking/workouts"

sheety_get_url = f"{sheety_url}{sheety_endpoint}"

sheety_headers = {
    "Authorization": "Basic YWJoZTp3b3JraGFyZEAxMzUyNDY="
}

date_today = dt.datetime.now()

sheety_post_body = {
    "workout":{
      "date": date_today.strftime("%d/%m/%Y"),
      "time": date_today.strftime("%H:%M:%S"),
      "exercise": excersice_type,
      "duration": duration_min,
      "calories": calories_burned
    }
    }
sheet_resp = requests.post(url=sheety_get_url, json=sheety_post_body, headers=sheety_headers)
#sheet_resp = requests.get(url=sheety_get_url)
sheet_resp.raise_for_status()
print(sheet_resp.text)