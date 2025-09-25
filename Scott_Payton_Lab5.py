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

def compare_power(data):
    """Compare power levels of two characters by name."""
    name1 = input("Enter the first character's name: ").strip()
    name2 = input("Enter the second character's name: ").strip()

    char1 = next((c for c in data if name1.lower() in c.get("name", "").lower()), None)
    char2 = next((c for c in data if name2.lower() in c.get("name", "").lower()), None)

    if not char1 or not char2:
        print("One or both characters not found!")
        return

    print(f"\n{char1['name']} (Max Ki: {char1.get('maxKi', 'Unknown')})")
    print(f"{char2['name']} (Max Ki: {char2.get('maxKi', 'Unknown')})")

    try:
        ki1 = int(char1.get("maxKi", "0").replace(",", ""))
        ki2 = int(char2.get("maxKi", "0").replace(",", ""))
    except ValueError:
        print("Error: Could not compare power levels.")
        return

    if ki1 > ki2:
        print(f"\n {char1['name']} is stronger!")
    elif ki2 > ki1:
        print(f"\n {char2['name']} is stronger!")
    else:
        print("\n They have equal power!")

    

def main():
    print("Welcome to the DragonBall Character Database! \n What would you like to do?!")

    
if __name__ == "__main__":
    main()