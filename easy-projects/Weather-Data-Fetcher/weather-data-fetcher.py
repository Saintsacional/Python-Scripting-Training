import requests
import json

# Define the API endpoint and your API key
API_KEY = <>  # Replace with your OpenWeatherMap API key
BASE_URL = <>

# Function to fetch weather data
def get_weather(city):
    # Define parameters for the request
    params = {
        'q': city,            # City name
        'appid': API_KEY,     # API key
        'units': 'metric',    # Temperature in Celsius
        'lang': 'en'          # Language of the response
    }

    # Send GET request to the API
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display weather info
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        # Optionally, you can save the data to a file
        with open('weather_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    else:
        print(f"Error fetching data: {response.status_code}")

# Example usage
city = input("Enter city name: ")
get_weather(city)
