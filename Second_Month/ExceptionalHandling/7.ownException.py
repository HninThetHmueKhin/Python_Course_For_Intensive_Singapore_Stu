class myExcept(Exception):
    pass
class NameError(myExcept):
    pass
class ValueError(myExcept):
    pass

try:
    a = 10
    b = 10
    if a is b:
        raise ValueError
    else:
        raise NameError
except NameError:
    print("Name Error")
except ValueError:
    print("Value Error")