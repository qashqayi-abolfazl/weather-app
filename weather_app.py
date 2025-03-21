﻿import tkinter as tk
import requests

# OpenWeatherMap API Key
API_KEY = "7ea63ee02b58aba915c4bb1d39874e41"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Create the main application window
root = tk.Tk()
root.title("Weather App")  
root.geometry("300x200")

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        weather_label.config(text="Please enter a city name")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        weather_label.config(text=f"🌡️ Temp: {temp}°C\n☁️ {description}\n💧 Humidity: {humidity}%")
    else:
        weather_label.config(text="❌ City not found!")



# Create a label
label = tk.Label(root, text="Enter City:", font=("Arial", 12))
label.pack(pady=5)


# Create an entry field
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

# Create a button and link it to get_weather()
get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_btn.pack(pady=5)

# Create a label to show weather data
weather_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
weather_label.pack(pady=10)


# Run the application
root.mainloop()
