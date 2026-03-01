from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Answer 'yes' if number is even, otherwise answer 'no'.")
    for n in range(3):
        num = randint(1, 100)            
        if num % 2 == 0:
            answer = "yes"
        else:
            answer = "no"
        print(f"Question: {num}")
        retarded_answer = prompt.string("Your answer: ")
        if retarded_answer != answer:
            print(f"'{retarded_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
