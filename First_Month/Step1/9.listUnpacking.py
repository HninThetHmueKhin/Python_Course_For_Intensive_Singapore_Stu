#list unpacking
# a = 10
# b =20
# c = 30
# print(a)
# print(b)
# print(c)

a1,a2,a3 = 10,20,30#tuple
print(a1,a2,a3)

a,b,*c,d=[1,2,3,4,5,6,7,8,9]#default tuple
#too many values to unpack (expected 2)
print(a,b)
print(c)
print(d)