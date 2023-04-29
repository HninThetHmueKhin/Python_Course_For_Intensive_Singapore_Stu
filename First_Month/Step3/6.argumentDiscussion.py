#4
#Default argument
#Keyword argument (named argument)
#Positional Argument
#Arbitrary argument (*args and **kwargs)
#*kwargs ---> arbitrary keyword argument

def student(name,age,school="Harvard",grade='A'):#function definition ---> parameter
    """default argument testing"""
    print("Student Details: ",name,age,grade,school)
student('John',24)#fun call ---> argument
print(student.__doc__)

def student1(name,age):
    """Keyword argument testing"""
    print("Student Details: ",name,age)
student1(name="kelvin",age=24)

"""positional arg"""
def subtract(a,b):
    print(a-b)
subtract(7,8)
subtract(a=8,b=7)#keyword argument

"""*args"""
def percentage(*args):
    sum = 0
    for i in args:  # 40
        sum += i  # 90
    avg = sum/len(args)#90/3=30.0
    print("Average: ",avg)
percentage(20,30,40)

"""**kwargs"""
#key-value pair like dictionary

def percentage1(**kwargs):
    sum = 0
    for i in kwargs:
        sub_name = i
        sub_marks = kwargs[sub_name]
        print(sub_name,"=",sub_marks)
        sum+=sub_marks
    avg = sum/len(kwargs)
    print("Average : ",avg)

percentage1(english=56,math=61,chemistry=70)


