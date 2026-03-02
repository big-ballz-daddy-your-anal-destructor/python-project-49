from random import randint

description = ("Answer 'yes' if given number is prime. Otherwise answer 'no'.")


def game():
    num = randint(3, 10)            
    for i in range(2, num // 2 + 2):
        if num % i == 0:
            answer = "no"
            break
        else:
            answer = "yes"
    question = num
    return question, answer