from cli_box import rounded
from sys import exit
from rpsfunc import game
startcom = ['rock', 'paper', 'scissors']
quitcom = ['Q', 'q']
userscore = 0
compscore = 0
while True:
    start = input("Welcome to my Rock, Paper, Scissors Game! Pick between Rock/Paper/Scissors to Start or Q to Quit: ")
    if start.lower() in startcom:
        game(start.lower())
    elif start in quitcom:
        print(rounded("Maybe next time! Goodbye!"))
        exit()
    else:
        print(rounded("I didn't understand that! Can you reply in Rock/Paper/Scissors to Start or Q to Quit"))
        