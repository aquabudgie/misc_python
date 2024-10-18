import requests

# Your API key
api_key = ""

# Coordinates for the location
lat = 
lon = 

# URL for the API request
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"

# Making the request
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    # print(response)
