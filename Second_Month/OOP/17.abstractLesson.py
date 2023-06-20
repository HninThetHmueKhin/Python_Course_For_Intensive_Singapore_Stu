"""
without body only header ---> abstract method ---> fast

implements body<--
"""
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def normal(self):
        print("Hi I am normal method")

class Dog(Animal):
     def speak(self):
         print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.speak()
    cat.speak()
    dog.normal()
    cat.normal()
