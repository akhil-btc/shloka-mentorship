import requests


def show_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 19.0760,    # Mumbai
        "longitude": 72.8777,
        "current_weather": True,
    }

    response = requests.get(url, params=params)
    profile = response.json()

    temperature = profile["current_weather"]["temperature"]

    if temperature < 18:
        print("Stay Warm.")
    elif temperature <= 28 and temperature >= 18:
        print("Nice day for a walk.")
    elif temperature > 28:
        print("Stay hydrated.")


def show_quote():
    url1 = "https://zenquotes.io/api/random"

    response1 = requests.get(url1)
    profile1 = response1.json()

    print(profile1[0]["q"])


show_quote()
show_weather()