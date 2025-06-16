import requests

def get_weather(location):
    user_location = location
    url = f'https://api.openweathermap.org/data/2.5/weather?q={user_location}&appid=b3fb8dce342fb85351d39f4b011756a4&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
      raise Exception("City not found. Please check the name and try again.")
    else:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        conditions = data["weather"][0]["description"]

    return temperature, humidity, conditions

def main():
    location = input("Enter your location: ").strip().title()
    try:
        temperature, humidity, conditions = get_weather(location)
        print(f"{location} Weather:")
        print(f"- Temperature: {temperature}°C\n- Humidity: {humidity}%\n- Conditions: {conditions.capitalize()}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
