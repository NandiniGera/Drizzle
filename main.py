import json
import os
from weather import get_weather
from compare_weather import compare_weather, get_weather_data
from completer import CityNameCompleter;
from prompt_toolkit import prompt

CONFIG_FILE = "config.json"

def get_user_info():
    if os.path.isfile(CONFIG_FILE):
        try:

            with open(CONFIG_FILE, "r") as file:
                config_data = json.load(file)
                name = config_data.get("name")
                default_location = config_data.get("location")

        except (json.JSONDecodeError, FileNotFoundError):

            print("Invalid or empty JSON file. Starting from scratch.")
            name = input("Enter your name: ")
            default_location = prompt("Enter city name: ", completer=CityNameCompleter())
            print("You entered:", default_location)
    else:
        
        name = input("Enter your name: ")
        default_location = prompt("Enter your default location: ", completer=CityNameCompleter())
        print("You entered:", default_location)
        

    print(f"Hey {name}. Welcome back! Choose an option:\n")
    print("1. Use default location")
    print("2. Use a new location")
    print("3. Compare weather of two locations")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "2":
        location = prompt("Enter the new location: ", completer=CityNameCompleter())
        print("You entered:", location)
        get_weather(location)
        
    elif choice == "3":
        city1 = prompt("Enter the first city name: ", completer=CityNameCompleter())
        print("You entered:", city1)
        city2 = prompt("Enter the second city name: ", completer=CityNameCompleter())
        print("You entered:", city2)
        
        weather_data_city1 = get_weather_data(city1)
        weather_data_city2 = get_weather_data(city2)
        compare_weather(city1, weather_data_city1, city2, weather_data_city2)
        
    elif choice == "1":
        location = default_location
        get_weather(location)

    with open(CONFIG_FILE, "w") as file:
        config_data = {"name": name, "location": location}
        json.dump(config_data, file)

def main():
    get_user_info()

if __name__ == "__main__":
    main()