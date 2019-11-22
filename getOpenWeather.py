# Prints weather for a location from the command line

APPID = '[REDACTED]'

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see raw json data
# print(response.text)

# Load JSON data into Python variable
weatherData = json.loads(response.text)

# Print weather description
w = weatherData['list']
print(f'5 day forecast for {location}:')
for i in range(5):
    print(f'Day {i+1}')
    print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'])
    print()