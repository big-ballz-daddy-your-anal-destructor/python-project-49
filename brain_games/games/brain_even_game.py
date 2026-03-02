from random import randint

description = 'Answer "yes" if number is even, otherwise answer "no".'


def game():
    question = randint(1, 100)            
    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return question, answer