#function ထဲရှိ arg
#def myFun(a:'annotation of a',b:'annotation of b')->'return of function'
def myFun(a:'annotation of a',b:'annotation of b')->'return of function':
    """This is body expression of myFun"""
    return a * b
print(myFun.__annotations__)
print(myFun.__doc__)

#another function
x = 3
y =5
def myFun1(a:'some value from funCall')->'multiply'+str(max(x,y))+'times':
    """This function will return multiply of max"""
    return a*max(x,y)
print(myFun1.__annotations__)
result = myFun1(2)
print(result)

def myFun2(a:'some value from funCall',b:'some value from funCall')->'b'+'a'+'multiply'+str(max(x,y))+'times':
    """This function will return b plus a multiply of max"""
    return b+a*max(x,y)
data1 = myFun2(2,4)
print(data1)
print(myFun2.__annotations__)
print(myFun2.__doc__)