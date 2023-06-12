#with statement ---> exception ---> file auto off

with open('data1.txt','r') as file:
    if file:
        contents = file.read()
        print(contents)
    else:
        print("something wrong")