#ternary operator
def is_adult(age):
    if age>18:
        return True
    else:
        return False

check = is_adult(19)
print(check)

def is_adult2(age):
    return True if age>18 else False

print(is_adult2(17))