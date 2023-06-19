import os
# os.chdir('/Users/khine/Desktop/')

parent_dir = "/Users/khine/"

directory = "Desktop/OS-Sample/"

path = os.path.join(parent_dir,directory)

print("Path: ",path)

os.mkdir(path)

print(os.listdir())
# print(os.listdir())