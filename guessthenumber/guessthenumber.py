from ascii_art import logo
import random

EASY_LEVEL_TURNS = 12
HARD_LEVEL_TURNS = 6


def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it. The answer was {answer}")


def set_difficulty():
    level = input("Choose difficulty 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to Number Guessing Game")
    print("Think a number between 1 to 100....")
    turns = set_difficulty()
    answer = random.randint(1, 100)
    # print(f"THE ANSWER IS {answer}")

    guess_number = 0
    while guess_number != answer:
        if turns == 0:
            print(f"You lost..... The number was {answer}")
            return
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_number = int(input("Guess a number: "))
        turns -= 1
        check_answer(guess_number, answer)


print(logo)
game()
