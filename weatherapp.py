import requests

def get_weather(city):
    api_key = "65179fc844792f2a9a7c0c727de9cb7b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return "Error: Failed to fetch weather data"

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    return {
        'description': weather_description,
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed
    }

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    if isinstance(weather_data, str):
        print(weather_data)
    else:
        print("Weather Information:")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {weather_data['temperature']} K")
        print(f"Humidity: {weather_data['humidity']} %")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

if __name__ == "__main__":
    main()
