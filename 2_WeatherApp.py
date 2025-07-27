import json
import requests

city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=a97c8ffacb42406eb6b153706222401&q={city}"
r = requests.get(url)
print(r.text)
