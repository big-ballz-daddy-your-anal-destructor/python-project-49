from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    question = randint(1, 100)  #NOSONAR            
    if question % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return question, answer