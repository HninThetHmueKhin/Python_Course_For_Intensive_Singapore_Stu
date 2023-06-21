try:
    data = int(input("Enter a valid key: "))
# except Exception as err:
#     print(err)
except ValueError as err:
    print(err)
finally:
    print("This else statement is running")