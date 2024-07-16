import requests
from datetime import datetime

# User and API details in U.S. customary units
GENDER = ""#Your Gender
WEIGHT_LBS = #Your weight
HEIGHT_FT = #Your height
HEIGHT_IN = #Your height
AGE = #Your age

# Convert U.S. customary units to metric
WEIGHT_KG = WEIGHT_LBS * 0.453592
HEIGHT_CM = (HEIGHT_FT * 12 + HEIGHT_IN) * 2.54

APP_ID = ""#Your APP ID
API_KEY = ""#Your API KEY

nutr_endpoint = ""#Your nutritionix.com
sheety_endpoint = ""#Your https://sheety.co/

exercise_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Perform POST request to Nutritionix API
response = requests.post(nutr_endpoint, json=params, headers=headers)
result = response.json()
print("Nutritionix API Response:")
print(result)

# Check if the 'exercises' key is in the result
if 'exercises' in result:
    exercises = result['exercises']
else:
    print("Key 'exercises' not found in the Nutritionix API response.")
    exercises = []

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Assuming result from Nutritionix API contains the needed details
for exercise in exercises:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Perform POST request to Sheety API
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    if sheet_response.status_code == 201:
        new_entry = sheet_response.json()
        print("New entry added to Sheety:")
        print(new_entry['workout'])
    else:
        print(f"Failed to add data to Sheety: {sheet_response.status_code}, Message: {sheet_response.json().get('message')}")
