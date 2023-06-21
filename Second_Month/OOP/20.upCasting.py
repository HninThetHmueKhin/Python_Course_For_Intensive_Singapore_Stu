class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

if __name__ == '__main__':
    dog = Dog()
    dog.sound()

    #upcasting
    # animal = Animal()
    # animal.sound()
    animal = dog
    animal.sound()
