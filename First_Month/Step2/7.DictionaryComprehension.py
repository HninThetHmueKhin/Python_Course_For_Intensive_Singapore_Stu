#Dictionary comprehension
my_dict = {"first":1,"second":2,"third":3}

new_dict = {k:v*2 for k,v in my_dict.items()}
print(new_dict)

new_dict1 = {k.upper():v for k,v in my_dict.items()}
print(new_dict1)

#list to dictionary comprehension
my_new_list = [1,2,3,4,5]
new_dict2 = {num:num*2 for num in my_new_list}
print(new_dict2)

#even/odd
new_dict3 = {i:("even" if i%2 ==0 else "odd") for i in my_new_list}
print(new_dict3)