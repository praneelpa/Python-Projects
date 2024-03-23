from cli_box import rounded
from sys import exit
startcom = ['rock', 'paper', 'scissors']
while True:
    start = input("Welcome to my Rock, Paper, Scissors Game! Pick between Rock/Paper/Scissors to Start or Q to Quit: ")
    if start.lower() in startcom:
        ...
    elif start == 'Q'.lower():
        print(rounded("Maybe next time! Goodbye!"))
        exit()
    else:
        print(rounded("I didn't understand that! Can you reply in yes or no?"))
        