import cli_box
import sys
import random

affirmative_responses = ['yes', 'y', 'why not', 'sure', 'i do', 'ya']
negative_responses = ['no', 'n', 'nope', 'nah', 'i dont', 'i do not', "i don't"]

goodjob = ["Good job!", "You did it!", "That's right", "Correct!", "Hurray! You got it"]
badjob = ["That's incorrect!", "Good luck next time", "Wrong!", "Try again next time!"]
score = 0

def random1():
    score1 = 0
    tries = 3
    while True:
        number1 = random.randint(1, 5)
        try:
            guess1 = int(input("Guess the number between 1 and 5: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if guess1 == number1:
            score += 1
            print(f"{random.choice(goodjob)} Your score is now {score}")
            random2()
            break
        elif guess1 != number1:
            tries -= 1
            print(f"{tries} more {'tries' if tries > 1 else 'try'}!")
            if tries == 0:
                print(f"No more tries! You fail! The correct number was {number1}")
                return score1
            sys.exit()

def random2():
    score2 = 0
    tries = 5
    while True:
        number2 = random.randint(1, 10)
        try:
            guess2 = int(input("Guess the number between 1 and 10: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if guess2 == number2:
            score += 2
            print(f"{random.choice(goodjob)} Your score is now {score}")
            random3()
            break
        elif guess2 != number2:
            tries -= 1
            print(f"{tries} more {'tries' if tries > 1 else 'try'}!")
        while tries == 0:
            print(f"No more tries! You fail! The number was {number2}")
            return score2
        sys.exit()

def random3():
    score3 = 0
    tries = 7
    while True:
        number3 = random.randint(1, 15)
        try:
            guess3 = int(input("Guess the number between 1 and 15: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if guess3 == number3:
            score += 3
            print(f"{random.choice(goodjob)} Your score is now {score}")
            random4()
            break
        elif guess3 != number3:
            tries -= 1
            print(f"{tries} more {'tries' if tries > 1 else 'try'}!")
        while tries == 0:
            print(f"No more tries! You fail! The number was {number3}")
            return score3
        sys.exit()

def random4():
    score4 = 0
    tries = 10
    while True:
        number4 = random.randint(1, 20)
        try:
            guess4 = int(input("Guess the number between 1 and 20: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if guess4 == number4:
            score += 4
            print(f"{random.choice(goodjob)} Your score is now {score}")
            random3()
            break
        elif guess4 != number4:
            tries -= 1
            print(f"{tries} more {'tries' if tries > 1 else 'try'}!")
        while tries == 0:
            print(f"No more tries! You fail! The number was {number4}")
            return score4
        sys.exit()

def game():
    print(cli_box.rounded("Let's start! You will be promoted to the next difficulty as you do better."))
    random1()

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
