import json
myPython = {
  "name" : "khine",
  "age" : 25,
  "hobby" : ["coding","training","building IOT"]
}

with open("jdataFile.json","w") as jsFile:
    json.dump(myPython,jsFile,indent=2,sort_keys=True)