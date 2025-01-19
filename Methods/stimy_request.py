import requests
import json
import os

message = "solve 8x=2"
solution = ""
json_type = "solution_text"
STIMY_KEY = os.getenv("STIMY_KEY")
# print(STIMY_KEY)

def send_http_request(url, api_key, payload):
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload)
    return response


def get_answer(message):
    url = "https://dtvrspmgsb4uh.cloudfront.net/solve"
    api_key = STIMY_KEY

    payload = {
        "problem": {
            "type": "text",
            "data": message
        },
        "language": "en-US"
    }

    response = send_http_request(url, api_key, payload)

    if response.status_code == 200:
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.json())
        print(json.dumps(response.json(), indent=4))
        solution_text = response.json().get("solution_text")
        print("Solution Text:", solution_text)
    else:
        print("Failed to get a response. Status Code:", response.status_code)
        print("Response Body:", response.text)

# message = "Identify the coefficients of the following quadratic expression: 2x^2 - 5x + k = 0"
# get_answer(message)