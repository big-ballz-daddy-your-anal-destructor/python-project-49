from random import randint

description = ("Find the greatest common divisor of given numbers.")


def game():
    num1 = randint(1, 10)  #NOSONAR
    num2 = randint(1, 10)  #NOSONAR
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
    question = f'{num1} {num2}'
    return question, answer