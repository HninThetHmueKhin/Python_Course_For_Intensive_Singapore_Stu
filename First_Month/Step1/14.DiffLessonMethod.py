#list methods
#accessing list items
myList = ["juice","glasses","flower","glasses"]
print(myList[0])

#change list items
myList[1] = "blueberry"
print(myList)

myList[1:3] = ["green","red"]
print(myList)

#insert elements
myList.insert(4,"index4")
print(myList)

#add list elements
myList.append("book")
print(myList)

newList = ["new1","new2"]
myList.extend(newList)
print(myList)

#remove
myList.remove("new1")
print(myList)

#loop list
for x in myList:
    print(x)

for i in range(len(myList)):
    print(myList[i])

#while lkoop
i = 0
while(i<len(myList)):
    print(myList[i])
    i+=1