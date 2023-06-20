"""
Python	JSON
---------------------
dict	object
list, tuple	array
str	string
int, long, float	number
True	true
False	false
None	null

JSON ---> JavaScript Object Notation

Json Encoding(Serialization)
json.dumps() : Convert Python object to JSON string
json.dump() : Write Python object to a file in JSON format

JSon Decoding(Deserialization)
json.loads(): Convert Json string to python object
json.load(): Read a Json file and convert it to a Python object
"""
#https://docs.python.org/3/library/json.html
#https://jsonlint.com/
import json
myJson = """
{
  "name" : "khine",
  "age" : 25,
  "hobby" : ["coding","training","building IOT"]
}
"""
data = json.loads(myJson)#convert from json to python
print(data,type(data))
for key,value in data.items():
    print(value)
print(data['name'])

