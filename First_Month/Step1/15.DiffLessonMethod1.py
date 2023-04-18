#List comprehension
myList = ["juice","glasses","flower","glasses"]
newList = []
# for x in myList:
#     if 'juice' in myList:
#         newList.append(x)
# print(newList)

newList = [x for x in myList if 'juice' in myList]
print(newList)

#Syntax
#newList = [expression for item in iterable if condition==True]

#other eg
mynewList = range(5)# 0 1 2 3 4
print(range(5))
# for x in mynewList:
#     if 4 in mynewList:
#         newList.append(x)
# print(newList)
newList = [x for x in mynewList if 4 in mynewList]
print(newList)