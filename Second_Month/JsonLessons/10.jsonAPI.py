import json
import requests
from random import randint

food_choice = input("Please enter your choice: ")
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'
r = requests.get(url)
data = json.loads(r.text)
print(data)


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

value = randint(0,len(beer_list)-1)
print(value)
try_this = beer_list[value]
try_name = try_this['new_name']
try_tagline = try_this['new_tagline']
try_abv = try_this['new_abv']
print(f'You shoud try {try_name},{try_tagline} ,{try_abv}%')
