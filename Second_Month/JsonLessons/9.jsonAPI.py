#https://punkapi.com/
import json
import requests

url = "https://api.punkapi.com/v2/beers?food=burger"
r = requests.get(url)
data = json.loads(r.text)

beer_list = []
for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']
    beer_items = {
        'new_name' : name,
        'new_tagline':tagline,
        'new_abv' : abv
    }
    beer_list.append(beer_items)
print(beer_list)
