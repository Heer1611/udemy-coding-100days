import requests
from datetime import datetime
import smtplib

MY_LAT = #Your Latitude
MY_LONG = #your Longitude

def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False

def at_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_time = datetime.fromisoformat(sunrise[:-1])
    sunset_time = datetime.fromisoformat(sunset[:-1])
    time_now = datetime.now().hour

    if time_now < sunrise_time or time_now > sunset_time:
        return True
    return False

def send_email():
    # Update the following with your email credentials
    my_email = ""#your_email@gmail.com
    my_password = ""#your_password
    recipient_email = ""#recipient_email@gmail.com

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
        )

if iss_above() and at_night():
    send_email()
