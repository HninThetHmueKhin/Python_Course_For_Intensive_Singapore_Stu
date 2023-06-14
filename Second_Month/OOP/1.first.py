class Person:
   #special method
   def __init__(self):#default constructor
       print("Welcome")

   def __init__(self,name):#one parameter constructor
       print(name)

   def __init__(self,name,age):#two parameter constructor
       print(name,age)

if __name__ == '__main__':
    obj = Person("KZT",21)