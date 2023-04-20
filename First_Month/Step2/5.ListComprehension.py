myStr = "Hello"
# myList = []
# for c in myStr:
#     myList.append(c)
# print(myList)

#comprehension
myList = [c for c in myStr]
print(myList)

numbers = [1,2,3,4,5,6]
myList1 = [num*2 for num in numbers]
print(myList1)