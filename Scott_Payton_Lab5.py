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


def main():
    print("Welcome to the DragonBall Character Database! \n Here youa are able to do many things, elts get started!")
    

if __name__ == "__main__":
    main()