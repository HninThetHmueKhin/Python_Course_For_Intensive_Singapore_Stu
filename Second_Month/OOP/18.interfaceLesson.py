"""pip install zope.interface"""
"""all abstract method ---> slow"""
import zope.interface

class MyInterface(zope.interface.Interface):
    def method1(self):
        pass

    def method2(self):
        pass

    # def normal(self):
    #     print("Hi I am normal")

@zope.interface.implementer(MyInterface)
class derivedClass:
    def method1(self):
        print("Hello")

    def method2(self):
        print("Method2")

if __name__ == '__main__':
    # print(type(MyInterface))
    # print(MyInterface.__module__)
    # print(MyInterface.__name__)

    der  = derivedClass()
    der.method1()
    der.method2()
    der.normal()