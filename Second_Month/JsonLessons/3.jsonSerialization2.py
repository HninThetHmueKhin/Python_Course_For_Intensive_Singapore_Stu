import json
myJson = {
  "name" : "khine",
  "age" : 25,
  "hobby" : ["coding","training","building IOT"]
}

with open("jdataFile.json","w") as jsFile:
    json.dump(myJson,jsFile,indent=2,sort_keys=True)