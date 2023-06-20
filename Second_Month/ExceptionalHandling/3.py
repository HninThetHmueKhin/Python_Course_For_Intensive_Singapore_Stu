try:
    file = open("myfile.txt")
    print(file)
# except FileNotFoundError as err:
#     print(err)
except OSError as err:
    print(err)
finally:
    print("Unexpected error:")