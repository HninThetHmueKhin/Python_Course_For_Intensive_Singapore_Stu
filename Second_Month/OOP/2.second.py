class Person:
   #special method
   def __init__(self,name,age):#default constructor
       # self.name = name
       # self.age = age
       print(f'{name} : {age}')

   def welcome(self):
       print(f'Welcome from python course')


if __name__ == '__main__':
    obj = Person("KZT",24)
    obj.welcome()
