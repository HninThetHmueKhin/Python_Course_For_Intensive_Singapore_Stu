"""
1.Arithmetic Operators
   +,-,*,/,//,%(Modulo),**(Power)
2.Assignment Operators
3.Comparison Operators
4.Logical Operators
5.Bitwise Operators
6.Special Operators
"""
"""
1.Arithmetic Operators
"""
a = 10
b = 3

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Muliplication:",a*b)
print("a to the power b",a**b)
print("Division: ",a/b)#9/3 = 3.0
print("Modulo result: ",a%b)
print("Floor division result: ",a//b)

"""
2.Assignment Operators
 =,+=,-=,*=,/=,%=,**=,//=
"""
creditScore1 = 10
creditScore2 = 10
print(creditScore1)#10
creditScore2+=10
#creditScore2 = creditScore2+10
creditScore2-=10
creditScore2*=2
creditScore2%=3
print(creditScore2)#20


"""
3.Comparison Operators
  ==,!=,>,<,>=,<=
"""
print(3==5)
print(3!=5)
print(3>5)
print(3<5)
print(3>=5)
print(5<=5)


"""
4.Logical Operators
  and , or,not
"""
boolVar = False
print("BoolVar: ",not(boolVar))

print(True and True)#True
print(True and False)#False
print(True or False)#True
print(not True)#False

"""
6.Special Operators 
  1.Identity Operators
     is,is not
  2.Membership Operators
    in,not in ---> string,list,tuple,set,dictionary
"""
#Identity Operators
#if int data type,string data types ---> same values---> equal as identical
#list [] ----> if they are list ---->they are equal  but not identical.
a1 = 5
a2 = 5
b1 = "Hello"
b2 = "Hello"
list1 = [1,2,3]
list2 = [1,2,3]

print("a1 is a2 : ",a1 is a2)
print("a1 is not a2 : ",a1 is not a2)
print("b1 is b2 : ",b1 is b2)
print("b1 is not b2 : ",b1 is not b2)


print("list1 is list2 : ",list1 is list2)
print("list1 is not list2 : ",list1 is not list2)


#Membership Operators
mem = "Member123"
print("1" in mem)
print("1234" not in mem)#True , False