from random import randint, choice

import prompt

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What number is missing in this progression?")
    for n in range(3):
        num1 = randint(1, 30)
        num2 = randint(1, 10)
        num3 = randint(0, 7)
        sign = choice(["+", "-"])
        prog = [num1]
        if sign == "+":
            for a in range(10):
                next_num = num1 + num2
                prog.append(next_num)
                num1 = next_num
        elif sign == "-":
            for b in range(10):
                next_num = num1 - num2
                prog.append(next_num)
                num1 = next_num
        answer = prog[num3]
        prog[num3] = ".."
        prog_in_str = []
        for c in prog:
            prog_in_str.append(str(c))
        prog_in_str_perfect = " ".join(prog_in_str)
        print(f"Question: {prog_in_str_perfect}")
        retarded_answer = prompt.string("Your answer: ")
        clean_users_answer = retarded_answer.strip().replace(" ", "")
        if clean_users_answer != str(answer):
            print(f"'{retarded_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")