from random import choice, randint

description = ("What number is missing in the progression?")


def game():
    num1 = randint(1, 30)  #NOSONAR
    num2 = randint(1, 10)  #NOSONAR
    num3 = randint(0, 7)  #NOSONAR
    sign = choice(["+", "-"])  #NOSONAR
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
    question = prog_in_str_perfect
    return question, answer