import random
from cli_box import rounded
choices = ['rock', 'paper', 'scissors']
def game(user):
    computer = random.choice(choices)
    if user == computer:
        print(rounded("It's a draw!"))
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print(rounded("You win!"))
    else:
        print(f"Computer chose {computer}.")
        print(rounded("Computer wins!"))

