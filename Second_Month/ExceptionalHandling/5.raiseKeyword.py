try:
    print("activating exception")
    a = 10/0
    raise ZeroDivisionError
except ZeroDivisionError:
    print("From ZeroDivision Error")