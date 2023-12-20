
from random import randint


def get_input():
    result = input("Enter Rock, Paper, or Scissors\n").lower()
    return result


def get_computer_input():
    computer_choices = ['rock', 'paper', 'scissors']
    number = randint(0, 2)
    choice1 = computer_choices[number]
    print(choice1)
    return choice1


def check_winner(user_choice, computer_choice):
    winner = False
    if (user_choice == 'rock' and computer_choice == 'rock') or (user_choice == 'paper' and computer_choice == 'paper') \
            or (user_choice == 'scissors' and computer_choice == 'scissors'):
        print("You have both picked the same thing")
        winner = False
        return winner
    elif (user_choice == 'rock' and computer_choice == 'paper') or (
            user_choice == 'paper' and computer_choice == 'scissors') or (
            user_choice == 'scissors' and computer_choice == 'rock'):
        print("The computer is the winner")
        winner = True
        return winner
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (
            user_choice == 'paper' and computer_choice == 'rock') or (
            user_choice == 'scissors' and computer_choice == 'paper'):
        print("The user is the winner")
        winner = True
        return winner
    else:
        print("You have incorrectly typed something")
        winner = False
        return winner


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    isWinner = False

    while not isWinner:
        user_input = get_input()
        choice = get_computer_input()
        isWinner = check_winner(user_input, choice)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
