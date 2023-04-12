user = {
    'name':'Khine',
    'gender':'female'
}
#accessing elements
print(user['gender'])#traditional
print(user.get('name'))#none if key doesn't exist in dictionary
print(user.get('nationality'))#None
print(user.get('nationality','myanmar'))#default value
print(user['name'])


password = {"mgmg":123,"koko":345}
print(password.get("mgmg"))
print(password.values())
print(type(password.values()))
print("++++++++++++++++++++++++++++++++++++++=")
#object
for i in password:#key only
    print(i)
for i in password.items():#key,value in tuple
    print(i)

for key,value in password.items():
    if value == 123:
        print("Success")
    print(f'{key} : {value}')

for i in password.values():
    print(i)
