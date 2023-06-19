"""
Types of Inheritance in python
---------------------------------
1.Single Inheritance
2.Multiple Inheritance
3.Multi-level Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance
"""
#Single Inheritance
class Machine:
    def __init__(self,id):
        self.id = id

    def start(self):
        print("Machine started")

    def stop(self):
        print("Machine stopped")

class Car(Machine):
    def __init__(self,id,name):
        super().__init__(id)
        self.name = name

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def changeGear(self):
        print("Gear Changed")

if __name__ == '__main__':
    car = Car(1,"BMW")
    car.start()
    car.changeGear()
    car.stop()

    machine = Machine(2)
    machine.start()
    machine.stop()



