import urllib.request
import json
def get_weather(city):
    api_key = "3c9fb6e6126a64705e3902bdc3301cd4"  
    base_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    url = base_url.format(city, api_key)
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        if data["cod"] == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")
    
    except Exception as e:
        print("Error fetching weather data:", e)

if __name__ == "_main_":
    city = input("Enter city name: ")
    get_weather(city)