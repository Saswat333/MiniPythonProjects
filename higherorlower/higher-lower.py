from art import logo
from art import vs
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guessval, a_followers, b_followers):
    if a_followers > b_followers:
        return guessval == "a"
    else:
        return guessval == "b"


print(logo)
round_score = 0
game_should_continue = True
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

while game_should_continue:
    account_a_old = account_a
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b or account_b == account_a_old:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower, b_follower)

    if is_correct:
        round_score += 1
        print(f"You are right !! Your score is {round_score}")
    else:
        game_should_continue = False
        print(f"Sorry !! You are wrong. Final score is {round_score}")

