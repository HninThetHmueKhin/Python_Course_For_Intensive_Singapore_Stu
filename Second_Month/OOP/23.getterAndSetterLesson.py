class Person:
    def __init__(self,name):
        self._name = name

    #getter method
    def get_name(self):
        return self._name

    #setter method
    def set_name(self,name):
        self._name = name

if __name__ == '__main__':
    person = Person("Jane")
    print(person.get_name())

    person.set_name("Alice")
    print(person.get_name())


