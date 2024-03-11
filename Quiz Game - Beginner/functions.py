import cli_box
import random
goodjob = ["Good job!", "You did it!", "That's right", "Correct!", "Hurray! You got it"]
badjob = ["That's incorrect!", "Good luck next time", "Wrong!", "Try again next time!"]
qAnda = {
    "What is the color of the sky? ": ["Blue"],
    "What do you use to see distant objects? ": ["Binoculars"],
    "What is the opposite of 'day'? ": ["Night"],
    "Which planet is known as the Red Planet? ": ["Mars"],
    "What is the main gas that we breathe in? ": ["Oxygen"],
    "What do plants need to grow? ": ["Sunlight", "water"],
    "What is the capital city of France? ": ["Paris"],
    "What is the largest mammal in the world? ": ["Blue whale"],
    "What is the opposite of 'hot'? ": ["Cold"],
    "Which season comes after winter? ": ["Spring"]
}
def game():
    start =  print(cli_box.rounded("Let's start!"))
    questions = list(qAnda)
    random.shuffle(questions)
    score = 0
    badjob_random = random.choice(badjob)

    for question in questions:
        user_answer = input(question)
        answers = qAnda[question]
        if user_answer.lower() in [i.lower() for i in answers]:
            print(random.choice(goodjob))
            score += 1
        else:
            correct_answers_str = ', '.join(answers)
            print(f"{badjob_random}, The correct answer was: {correct_answers_str}")
    
    percent = (score / 10) * 100
    
    print(cli_box.rounded("End of the quiz! Your score is given below!"))
    print(cli_box.rounded(f"Your score was {score} / 10. In percentage, {percent}%"))
    