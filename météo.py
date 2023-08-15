import requests

API_KEY = 'VOTRE_CLÉ_API_OPENWEATHERMAP'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def main():
    city_name = input("Entrez le nom de la ville : ")
    weather_data = get_weather(city_name)

    if weather_data['cod'] == 200:
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        print(f"Température à {city_name} : {temperature}°C")
        print(f"Description : {weather_description}")
    else:
        print("Erreur lors de la récupération des données météorologiques.")

if __name__ == "__main__":
    main()
