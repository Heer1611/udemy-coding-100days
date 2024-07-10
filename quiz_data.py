import requests

parameter = {
    "amount": 10,
    "type": "boolean"
}

try:
    response = requests.get(url="https://opentdb.com/api.php?", params=parameter)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()
    question_data = data["results"]
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
    question_data = []
except requests.exceptions.ConnectionError as err:
    print(f"Connection error occurred: {err}")
    question_data = []
except requests.exceptions.Timeout as err:
    print(f"Timeout error occurred: {err}")
    question_data = []
except requests.exceptions.RequestException as err:
    print(f"An unexpected error occurred: {err}")
    question_data = []
