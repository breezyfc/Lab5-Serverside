import requests
import os
import random

# API endpoint
API_URL = os.getenv("API_URL", "http://dragonball-api.com/api/characters")

def fetch_characters():
    """Fetch character data from the API and return the list of characters."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, dict) and "items" in data:
            return data["items"]
        return data
    else:
        print("Error:", response.status_code)
        return []

def show_character_details(char):
    """Print all available details about a character."""
    print("\n=== Character Details ===")
    for key, value in char.items():
        print(f"{key.capitalize()}: {value}")
    print("=========================\n")

def search_by_name(data, name):
    """Search for a character by name (case-insensitive)."""
    results = [char for char in data if name.lower() in char.get("name", "").lower()]

    if results:
        for char in results:
            show_character_details(char)  
    else:
        print("No characters found.")

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
        ki1 = int(str(char1.get("maxKi", "0")).replace(",", ""))
        ki2 = int(str(char2.get("maxKi", "0")).replace(",", ""))
    except ValueError:
        print("Error: Could not compare power levels (invalid values).")
        return

    if ki1 > ki2:
        print(f"\n{char1['name']} is stronger!")
    elif ki2 > ki1:
        print(f"\n{char2['name']} is stronger!")
    else:
        print("\nThey have equal power!")

def show_by_race(data):
    """Show characters based on their Race."""
    race_name = input("Enter the Race name (e.g., Saiyan, Namekian, Human): ").strip()
    race_chars = [char for char in data if race_name.lower() in str(char.get("race", "")).lower()]

    if race_chars:
        print(f"\n=== Characters of Race: {race_name} ===")
        for char in race_chars:
            show_character_details(char)
    else:
        print("No characters found for that Race.")

def random_character(data):
    """Generate a random character."""
    if not data:
        print("No data available.")
        return

    char = random.choice(data)
    show_character_details(char)

def main():
    print("Welcome to the DragonBall Character Database!")

    data = fetch_characters()
    if not data:
        print("Could not fetch characters. Exiting.")
        return

    while True:
        print("\nWhat would you like to do?")
        print("1. Search for a character by name")
        print("2. Compare the power of two characters")
        print("3. Show characters based on their Race")
        print("4. Generate a random character")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter character name: ").strip()
            search_by_name(data, name)
        elif choice == "2":
            compare_power(data)
        elif choice == "3":
            show_by_race(data)
        elif choice == "4":
            random_character(data)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
