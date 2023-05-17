"""
seek() ---> offset,whence
whence --> 0 ---> start
       ---> 1 ---> current file
       ---> 2 ----> end
"""
with open('data.txt','rb') as file:
    if file:
        data = file.read(10)
        print("The file pointer at initial content: ",file.tell())#0
        file.seek(2,2)#start 1---> current position 2->end
        print("The file pointer after 2 moves: ",file.tell())
        file.seek(5,1)
        print("The file pointer after 5 moves: ", file.tell())

        data = file.read(10)
        print("New content: ",file.tell())
        # file.seek(10,2)
        # print("The file pointer after backward 10 moves: ", file.tell())
    else:
        print("Something wrong")