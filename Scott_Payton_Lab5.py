import requests
import os
import sys

API_URL = os.getenv ("API_URL", "http://dragonball-api.com/api/characters")

def fetch_characters():
    """Fetch the characters from the API."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch characters.")
        sys.exit(1)

def search_by_name(data, name):
    """Search For Character By Name"""
    results = [char for char in data if name.lower() in char['name'].lower()]
    return results


def main():
    print("Welcome to the DragonBall Character Database! \n Here youa are able to do many things, elts get started!")


    

if __name__ == "__main__":
    main()