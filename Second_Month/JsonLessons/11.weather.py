import json
import requests
#https://openweathermap.org/api
keys = '81d9fa83140eb4c5be0084535881fc9e'
#https://api.openweathermap.org/data/2.5/weather?q=Yangon&appid=81d9fa83140eb4c5be0084535881fc9e
url = 'https://api.openweathermap.org/data/2.5/weather?appid=81d9fa83140eb4c5be0084535881fc9e&q='
cityName = input("Please enter your city name: ")
newUrl = url + cityName

#method 1
# jsonData = requests.get(newUrl).json()
# print(type(jsonData))
# print(jsonData)

#method 2
jsonData = requests.get(newUrl).json()
print(type(jsonData))
for i in jsonData:
    print(i)
print(jsonData['coord'])