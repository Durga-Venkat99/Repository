import requests

# Your OpenWeatherMap API key
API_KEY = "6782593558af93a1bf94abf167ce179c"

# Base URL for current weather data
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# Get user input for the city
city = input("Enter your city: ")

# Build the URL for the API request with country code
url = f"{BASE_URL}q={city},IN&appid={API_KEY}"

# Send the request to the API
response = requests.get(url).json()
# Check if 'main' key is present in the response
if 'main' in response:
    # Access temperature information
    current_temp = response['main']['temp']
    feels_like_temp = response['main']['feels_like']
    max_temp = response['main']['temp_max']
    min_temp = response['main']['temp_min']

    # Print the temperature information
    print("Current Temperature:", current_temp)
    print("Feels Like Temperature:", feels_like_temp)
    print("Maximum Temperature:", max_temp)
    print("Minimum Temperature:", min_temp)
else:
    print("Error: 'main' key not found in the response.")