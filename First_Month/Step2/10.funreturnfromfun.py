#return function from a function
def square(a):
    return a**2

def cube(b):
    return b**3

#fun call
def num(number):
    if number == 1:
        return square#fun return
    else:
        return cube

if __name__ == '__main__':
    sq = num(1)
    print(sq(10))
    cu = num(2)
    print(cu(3))

