# welcome in this video we are going to create weather checking program

# lets start with importing requests
import requests

#now import prity print as pprint
from pprint import pprint

# var for API_key we need api key see discription
API_key = 'f76d8c27bd0864338b08cc8138714d4d'

# input for city 
city = input("Enter the City : ")

# here we add url 
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_key +"&q=" + city

# here we store weather data
weather_data = requests.get(base_url).json()

# now we print the data 
pprint(weather_data)

# see the output.........

# thanks gor watching catch you in next in video
