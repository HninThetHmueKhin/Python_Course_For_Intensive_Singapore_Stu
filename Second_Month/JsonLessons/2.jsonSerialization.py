import json
myJson = {
  "name" : "khine",
  "age" : 25,
  "hobby" : ["coding","training","building IOT"]
}

with open("jdataFile.json","w") as jsFile:
    json.dump(myJson,jsFile)