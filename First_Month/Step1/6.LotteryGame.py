import sys
username = input("Enter your name: ")
print("Welcome from Lottery Game,{}!!!".format(username))
age = int(input("Enter your age: "))
if age>=18:
    user_amount = int(input("Please enter your amount: "))
    option = int(input("Press 1 to play game:Press 2 to quit: "))#length
    #
    while option == 1:
        play_amount = int(input("Please enter your play amount: "))
        if user_amount < play_amount:
            print("Insufficient amount")
            sys.exit()
        else:
            pass
else:
    print("You are not legal to play this game!")

# import random
# random_no = random.randint(0,99)
# print(random_no)
