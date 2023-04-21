#function --- resuable
def greet():
    print("Hello")

greet()

def area(width,height):
    return(width*height)
result = area(12,20)
print(result)

#default value or parameter
def greet1(name="Khine"):
    print(f'Hello {name}')
greet1()