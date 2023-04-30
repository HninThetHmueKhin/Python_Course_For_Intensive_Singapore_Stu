#higher Order function
#function ကို arg အနေနဲ့ယူပြီးတော့ အဲ့ function ကို return
def myFun(x,fn):
    return fn(x)#lambda 5:5**2

value = myFun(5,lambda y:y**2)
print(value)

#higher order function --> args , kwargs
def myFun1(fn,*args,**kwargs):
    return fn(*args,**kwargs)#lambda(2,3)

print(myFun1(lambda x,y:x**y,2,3))
print(myFun1(lambda x,y:x+y,2,y=20))
