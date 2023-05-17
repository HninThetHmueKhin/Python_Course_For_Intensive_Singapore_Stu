with open('data.txt',"r") as file:
    if file:
        print("The file pointer at byte",file.tell())
        contents = file.read()
        print("Pointer is at byte: ",file.tell())
    else:
        print("Something wrong")

#r ----> 0
#w  ---> 0
#a  ----> last