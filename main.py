import requests


API_KEY = 'be727924bed4a3fd6611f93cefce59a1'
CITY = input("ENTER CITY:")
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"humidity: {data['main']['humidity']}")
    print(f"wind: {data['wind']['speed']}")

else:
    print("Error:", data["message"])