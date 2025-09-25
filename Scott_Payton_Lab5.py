import requests
import os
import sys

API_URL = os.getenv ("API_URL", "http://dragonball-api.com/api/characters")
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)
else:
    print("Error:", response.status_code)

    