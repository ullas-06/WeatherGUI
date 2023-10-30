import tkinter as tk
from PIL import Image, ImageTk
import requests
import json
from API import API_KEY


def get_weather():
    city = city_entry.get()
    url = f"{API_KEY}={city}"
    r = requests.get(url)
    wdic = json.loads(r.text)

    temp_c = wdic['current']['temp_c']
    temp_f = wdic['current']['temp_f']
    wind_kph = wdic['current']['wind_kph']
    wind_mph = wdic['current']['wind_mph']
    condition_icon_url = wdic['current']['condition']['icon']

    temperature_label.config(text=f"Temperature (Celsius): {temp_c}°C\nTemperature (Fahrenheit): {temp_f}°F")
    wind_speed_label.config(text=f"Wind Speed (KPH): {wind_kph} KPH\nWind Speed (MPH): {wind_mph} MPH")



    # Load and display weather icon
    icon_response = requests.get(f"https:{condition_icon_url}", stream=True)
    if icon_response.status_code == 200:
        icon = Image.open(icon_response.raw)
        icon = icon.resize((364, 364), Image.LANCZOS)  # Adjust size as needed
        # Adjust size as needed
        icon_photo = ImageTk.PhotoImage(icon)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo


# Create GUI window
root = tk.Tk()
root.title("Weather Forecast")

# City entry
city_label = tk.Label(root, text="Enter the Name of the city")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Button to get weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Labels for displaying weather information
temperature_label = tk.Label(root, text="")
temperature_label.pack()

wind_speed_label = tk.Label(root, text="")
wind_speed_label.pack()

# Image label
image_label = tk.Label(root)
image_label.pack()

# Label for weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Run the GUI application
root.mainloop()