#function passing through a function
#function ထဲမှာ function ကို parameter အနေနဲ့ဖြတ်သွား
def square(a):
    return a**2

def cube(b):
    return b**3

def funTofun(fun,n):
    return fun(n)#square(3)

if __name__ == '__main__':
    a = funTofun(square,3)
    print("Calling square function: ",a)
    print(funTofun(square,8))

    b = funTofun(cube,4)
    print('Calling cube function: ',b)