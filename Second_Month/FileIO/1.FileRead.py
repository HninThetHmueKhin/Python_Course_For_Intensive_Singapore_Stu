"""
Readline   ---> return string
Readlines  ---> return list
"""
file = open('data.txt','r')
if file:
    print("Success of opening file")
    data = file.readlines()
    print("Reading data with readline")
    print(data)
    print(type(data))
else:
    print("Error")
file.close()
