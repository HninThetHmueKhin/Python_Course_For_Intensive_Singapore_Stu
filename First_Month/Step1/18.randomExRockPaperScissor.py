import random

def get_choice():
    user_choice = input("What is your choice? r for rock , p for paper, s for  scissor")
    computer_choice = ["r","p","s"]
    computer = random.choice(computer_choice)
    print("Computer choices: ",computer)

    if user_choice == computer:
        return "It is a tie"
    elif user_choice == "r":#r ----> p,s
        if computer == "p":
            return "Paper covers rock!You lose"
        elif computer == "s":
            return "Rock smashes scissors!You win"
    elif user_choice == 'p':#p -----> s,r
        if computer == "s":
            return "Scissors cuts paper!You win"
        elif computer == "r":
            return "Paper covers rock!You win"
    elif user_choice == "s":
        if computer == "p":
            return "Scissors cuts paper!You win"
        elif computer == "r":
            return "Rock smashes scissors!You lose"

if __name__ == '__main__':
    choice = get_choice()
    print(choice)