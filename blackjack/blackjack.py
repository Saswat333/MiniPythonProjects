import random
from blackjack_art import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    def calculate_score(cards):
        # blackjack condition 10 and 11 both in deck
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_score(user_scores, computer_scores):
        if user_scores == computer_scores:
            return "Its a draw."
        elif computer_scores == 0:
            return "Lose, opponent has BlackJack."
        elif user_scores == 0:
            return "Win with a blackjack."
        elif user_scores > 21:
            return "You went over, You lose"
        elif computer_scores > 21:
            return "Opponent score went over. You win."
        elif user_scores > computer_scores:
            return "You win "
        else:
            return "You lose."

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your card: {user_cards},current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
                calculate_score(user_cards)
            else:
                is_game_over = True

    """ computer will keep drawing card untill its score is more than 17 or above 21"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_score}, Computer's hand: {computer_score}")
    print(compare_score(user_score, computer_score))


"""
Game starts from here
"""
play_game()
