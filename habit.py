import requests
from datetime import datetime

USERNAME = "" #create your own
TOKEN = "" #create your own
GRAPH_ID = ""#make you own

pixela_endpoint = "https://pixe.la/v1/users"

user_prams = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment the line below to create the user (only need to run once)
# response = requests.post(url=pixela_endpoint, json=user_prams)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment the line below to create the graph (only need to run once)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

make_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How Many hours did you code today? 5.")
}

# Uncomment the line below to create the pixel
# response = requests.post(url=make_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

updated_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=updated_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Uncomment the line below to create the graph (only need to run once)
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)