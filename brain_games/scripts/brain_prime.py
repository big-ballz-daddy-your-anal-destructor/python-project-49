from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    for n in range(3):
        num = randint(3, 10)            
        for i in range(2, num // 2 + 2):
            if num % i == 0:
                answer = "no"
                break
            else:
                answer = "yes"
        print(f"Question: {num}")
        retarded_answer = prompt.string("Your answer: ")
        if retarded_answer != answer:
            print(f"'{retarded_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
