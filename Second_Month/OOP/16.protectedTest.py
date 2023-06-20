class Parent:
    def __init__(self,age):
        self._age = age

    def getData(self):
        print(self._age)

class Sub(Parent):
    def getData(self):
        print(self._age)

if __name__ == '__main__':
    sub = Sub(21)
    sub.getData()

    parent = Parent(22)
    parent.getData()

