'''10.b.Fetch weather data from the JSON
Write a python program to fetch current weather data from the JSON file'''

# importing requests and json
import requests, json

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Enter City name : ")
API_KEY = input("Enter your API_KEY : ")  # Enter your API Key
# API_KEY = "7bdccf825b7dd119a05ac2e0afaf1aaa"
# API_KEY = "51a45f3640543d030d1e78bd52d2649c"

# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # weather report
    report = data['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
    # showing the error message
    print("Error in the HTTP request")

