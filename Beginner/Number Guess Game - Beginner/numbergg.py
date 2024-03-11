import cli_box
import sys
from nggfunctions import game

affirmative_responses = ['yes', 'y', 'why not', 'sure', 'i do', 'ya']
negative_responses = ['no', 'n', 'nope', 'nah', 'i dont', 'i do not', "i don't"]
while True:
    welcome = input("Welcome to my number guessing game! You will have to guess a number based on the 4 difficulties. Do you want to play? ")
    if welcome.lower() in affirmative_responses:
        game()
    elif welcome.lower() in negative_responses:
        print(cli_box.rounded("Maybe next time! Goodbye!"))
        sys.exit()
    else:
        print(cli_box.rounded("I didn't understand that! Can you reply in yes or no?"))
        break