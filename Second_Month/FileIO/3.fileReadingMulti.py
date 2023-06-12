"""
Readline   ---> return string
Readlines  ---> return list
read       ---> str
"""
file = open('data.txt','r')
# content = file.read()
# print(content,type(content))

#read one line at a time
line = file.readline()
while line:
    print(line)
    line = file.readline()
file.close()