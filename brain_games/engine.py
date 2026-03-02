import prompt

from brain_games.cli import welcome_user


def run_a_game(description, game):
    name = welcome_user()
    print(description)
    for n in range(3):
        question, answer = game()
        print(f"Question: {question}")
        users_answer = prompt.string("Your answer: ")
        if str(users_answer.replace(" ", "")) != str(answer):
            print(
                f"'{users_answer}' is wrong answer ;(."
                f"Correct answer was '{answer}'."
                f"\nLet's try again, {name}!"
            )
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
