from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for n in range(3):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        divs1 = []
        divs2 = []
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                divs1.append(i)
        for j in range(1, num2 + 1):
            if num2 % j == 0:
                divs2.append(j)
        divs_common = set(divs1) & set(divs2)
        real_divs = list(divs_common)
        real_divs.sort()
        answer = str(real_divs[-1])
        print(f"Question: {num1} {num2}")
        retarded_answer = prompt.string("Your answer: ")
        if retarded_answer != answer:
            print(f"'{retarded_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")