from random import choice, randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    for n in range(3):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        sign = choice(["+", "-", "*"])
        if sign == "+":
            q = f"{num1} + {num2}"
            answer = num1 + num2
        elif sign == "-":
            q = f"{num1} - {num2}"
            answer = num1 - num2
        elif sign == "*":
            q = f"{num1} * {num2}"
            answer = num1 * num2
        print(f"Question: {q}")
        retarded_answer = prompt.string("Your answer: ")
        if (retarded_answer) != str(answer):
            print(f"'{retarded_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
