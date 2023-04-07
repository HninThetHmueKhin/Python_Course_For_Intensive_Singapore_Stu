import string
string1 = "Hello"
#          01234
#     -5-4-3-2-1
# print(len(string1))
# for i in string1:
#     print(i)
#string slicing
print(string1[1])
print(string1[2:4])#start,stop
print(string1[2:5])
print(string1[2:])#2 to the end
print(string1[:])#the whole
print(string1[:4])#start to index 3

#negative index
print(string1[-5])
print(string1[-5:-2])
print(string1[-2:])