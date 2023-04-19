#list
#ordered,changeable,allow duplicate value,can access with index no
myList = ["juice","glasses","flower","glasses"]
myList[0] = "apple"
print(myList)

#Tuple
#ordered,allow duplicates value,unchangeable,can access with index no
myTuple = ("flower","juice","glasses","glasses")
#myTuple[0] = "apple" # 'tuple' object does not support item assignment
print(myTuple)

#set
#unordered,unchangeable,can't access with index no,doesn't allow duplicate values
mySet = {"flower","juice","glasses","glasses"}
print(mySet)
#print(mySet[0])#'set' object is not subscriptable

#dictionary
#ordered,changeable,doesn't allow duplicate values
myDict = {
    "flower":"rose",
    "juice":"orange juice",
    "glasses":"sunglasses",
    "glasses": "sunglasses"
}
print(myDict)
myDict["flower"] = "jasmine"
print(myDict)

