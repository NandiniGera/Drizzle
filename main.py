import json
import os
import pystray
from PIL import Image
from weather import get_weather
from compare_weather import compare_weather, get_weather_data
from system_tray import system_tray

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
            default_location = input("Enter your default location: ")
    else:
        name = input("Enter your name: ")
        default_location = input("Enter your default location: ")

    print(f"Hey {name}. Welcome back! Choose an option:\n")
    print("1. Use default location")
    print("2. Open default location in system tray")
    print("3. Use a new location")
    print("4. Compare weather of two locations")
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == "3":
        location = input("Enter the new location: ")
        get_weather(location)
        
    if choice == "4":
        city1 = input("Enter the first city name: ")
        city2 = input("Enter the second city name: ")

        weather_data_city1 = get_weather_data(city1)
        weather_data_city2 = get_weather_data(city2)
        compare_weather(city1, weather_data_city1, city2, weather_data_city2)
        
    if choice == "1":
        location = default_location
        get_weather(location)
    
    if choice == "2":
        system_tray(default_location)
        

    with open(CONFIG_FILE, "w") as file:
        config_data = {"name": name, "location": location}
        json.dump(config_data, file)



def main():
    get_user_info()

if __name__ == "__main__":
    main()
