import random

def get_choice():
    user_choice = input("What is your choice? r for rock , p for paper, s for  scissor")
    computer_choice = ["r","p","s"]
    computer = random.choice(computer_choice)
    choices = {"player":user_choice,"computer":computer}
    return choices

def check_win(player,computer):
    if player == computer:
        return "It is a tie"
    elif player == "r":#r ----> p,s
        if computer == "p":
            return "Paper covers rock!You lose"
        elif computer == "s":
            return "Rock smashes scissors!You win"
    elif player == 'p':#p -----> s,r
        if computer == "s":
            return "Scissors cuts paper!You win"
        elif computer == "r":
            return "Paper covers rock!You win"
    elif player == "s":
        if computer == "p":
            return "Scissors cuts paper!You win"
        elif computer == "r":
            return "Rock smashes scissors!You lose"

if __name__ == '__main__':
    choice = get_choice()
    print("Player and computer choice: ",choice)
    print("Player choice: ",choice.get("player"))
    print("Computer choice: ",choice.get("computer"))

    result = check_win(choice.get("player"),choice.get("computer"))
    print(result)
