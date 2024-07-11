import requests
from twilio.rest import Client

OWM_Endpoint = "" # Your openweathermap.org
api_key = "" #your API Key from openweathermap.org
account_sid = "" # Your account_sid from twilio
auth_token = "" # Your auth_token from twilio



weather_params = {
    "lat": ,#your latitude
    "lon": , #your longitude
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status() 
weather_data = response.json()  
# print(weather_data["list"][0]["weather"][0])
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) <700:
        will_rian =True
if will_rian:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_="+1",#Number thats being send from 
     body="It's going to rain Today. Remember to bring an umberlla ☔.",
     to="+1"#your number
)
print(message.status)