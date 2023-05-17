"""
os.SEEK_SET
os.SEEK_CUR
os.SEEK_END
"""
import os
with open('data.txt',"r") as file:
    if file:
        data  = file.read(10)
        print("Current position",file.tell())
        file.seek(2,os.SEEK_SET)#beginning ---> 0
        print("Current moving 2 position",file.tell())
        file.seek(5,os.SEEK_CUR)
        print("After 5 moves",file.tell())
        file.seek(8,os.SEEK_END)
        print("From end to 8 position ", file.tell())

