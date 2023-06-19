"""
Multiple Inheritance
-------------------------
-derived class can inherit from more than one parent

Syntax:
class DerivedClass(BaseClass1,BaseClass2,......)
   #class body
"""
class Animal:#BaseClass1
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Flyable:#BaseClass2
    def fly(self):
        print(f'{self.name} is flying')

class Bird(Animal,Flyable):
    #Derived Class
    def __init__(self,name):
        super().__init__(name)

if __name__ == '__main__':
    bird = Bird("Sparrow")
    bird.eat()
    bird.fly()