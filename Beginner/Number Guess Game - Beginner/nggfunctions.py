import random
import cli_box
import rfunc
goodjob = ["Good job!", "You did it!", "That's right", "Correct!", "Hurray! You got it"]
badjob = ["That's incorrect!", "Good luck next time", "Wrong!", "Try again next time!"]
score = 0

def game():
    print(cli_box.rounded("Let's start! You will be promoted to the next difficulty as you do better."))
    score1 = rfunc.random1()


