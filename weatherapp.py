import requests

#API configuration (variable declaration)
api_key = '0fe3713543c9194daf86db72787f438a'
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

# params dictionary 'q' = location query paramter, include city name, or coordinates of location
# 'appid' is the parameter to pass the API key
# 'units' specifies the units for temperature, 'metric' will return the temperature in Celsius
# JSON - javascript object notation, a format used for storing and transimitting data
# JSON represents data as key-value pairs and supports various data types like strings, booleans, arrays and objects
# In Python, the json module is available in the standard library and provides functionalities for working with JSON data. It allows you to encode Python objects into JSON strings (serialization) and decode JSON strings into Python objects (deserialization). This enables you to easily read and write JSON data in Python programs.
# Python object -> string (serialisation)
#string -> python object (deserialisation)