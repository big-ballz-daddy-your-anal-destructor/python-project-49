from random import choice, randint


description = "What is the result of the expression?"

def game():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    sign = choice(["+", "-", "*"])
    if sign == "+":
        question = f"{num1} + {num2}"
        answer = num1 + num2
    elif sign == "-":
        question = f"{num1} - {num2}"
        answer = num1 - num2
    elif sign == "*":
        question = f"{num1} * {num2}"
        answer = num1 * num2
    return question, answer