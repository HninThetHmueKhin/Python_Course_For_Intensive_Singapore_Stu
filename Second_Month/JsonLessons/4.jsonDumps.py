"""
dump vs dumps
python ---> json --> encode

dump(python obj,jsonFile)
dumps(python obj)
"""
import json
myInfo = {
  "name" : "khine",
  "age" : 25,
  "hobby" : ["coding","training","building IOT"],
    "pro" : ["coding","training","building IOT"]
}
json_object = json.dumps(myInfo)
print(json_object)
print(type(json_object))