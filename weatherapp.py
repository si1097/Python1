import requests

#API configuration (variable declaration)
api_key = 'API KEY'
base_url = 'https://api.openweathermap.org/data/2.5/weather'


#User input for location
location = input("Enter location: ")

#API request
params = {'q': location, 'appid': api_key, 'units': 'metric'}
response = requests.get(base_url, params=params)
data = response.json()

#Display weather information
if response.status_code == 200:
    print("Weather in", data['name'] )
    print("Temperature:", data['main']['temp'], "°C")
    print("Condition:", data['weather'][0]['description'])
else:
    print("Error:", data['message'])
