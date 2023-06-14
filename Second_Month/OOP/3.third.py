class myClass:
    def __init__(self):
        print("Welcome from python course")

    def __init__(self,name):
        print(f"Welcome from python course {name}")

    def myFun(self):
        print("My function")

if __name__ == '__main__':
    obj1 = myClass("TTU")
    obj1.myFun()

    obj2 = myClass("KZT")
    obj2.myFun()

    print(id(obj1))
    print(id(obj2))

    if id(obj1) == id(obj2):
        print("Addresses are equal!")
    else:
        print("They are not equal!")