import os

def current_path():
    print("Current Working Directory Before: ")
    print(os.getcwd())

if __name__ == '__main__':
    current_path()

    os.chdir("../../")

    current_path()