from brain_games.cli import welcome_user

import prompt


def run_a_game(description, game):
    name = welcome_user()
    print(description)
    for n in range(3):
        question, answer = game()
        print(f"Question: {question}")
        users_answer = prompt.string("Your answer: ")
        if str(users_answer.replace(" ", "")) != str(answer):
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
