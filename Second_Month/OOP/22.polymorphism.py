"""
Polymorphism ---> loading,overriding

same name with different parameter ---> method overloading
"""

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def calculate_area(self,length,width):
        return length * width

class Circle(Shape):
    def calculate_area(self,radius):
        return 3.14 * radius * radius

if __name__ == '__main__':
    rectangle = Rectangle()
    circle = Circle()

    area_rectangle = rectangle.calculate_area(5,10)
    area_circle = circle.calculate_area(3)

    print("Area of rectangle: ",area_rectangle)
    print("Area of circle: ",area_circle)
