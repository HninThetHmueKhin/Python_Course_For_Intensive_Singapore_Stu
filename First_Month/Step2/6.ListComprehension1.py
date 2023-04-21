numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
#condition
newevenList = [num for num in numbers if num%2 ==0 ]
print(newevenList)

#nested condition
new_list1 = [num for num in numbers if num%2 == 0 if num%3 ==0]
print(new_list1)

#if else in list comprehension
new_list2 = [num if num%2 ==0 else num*2 for num in numbers]
print(new_list2)

students = ["Bo Bo","Aye Min","Min Min","Aye Myat","Ko Aung","Aung Aung"]
            #  0       1        2          3         4
new_name_list = [name for name in students if name[0] == 'K']
print(new_name_list)

