from logo import logo
import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

cash = 1000

def calculate_score(card_score):
    get_sum = sum(card_score)

    if 11 in card_score and get_sum > 21:
        card_score.remove(11)
        card_score.append(1)
    return get_sum


def compare(computer_score, user_score):
    if computer_score == user_score:
        return f"It's a draw. Score: {user_score}"
    elif computer_score == 21:
        return f"You lost! Computer won with a blackjack! Your score: {user_score}"
    elif user_score == 21:
        return f"You won with blackjack! Computer score: {computer_score}"
    elif user_score > 21:
        return f"You lost! You went over. Your score: {user_score}"
    elif computer_score > 21:
        return f"Computer lost! It went over. Computer score: {computer_score}"
    elif user_score > computer_score:
        return f"You won! Computer's score: {computer_score}. Your score: {user_score}"
    else:
        return f"Computer won! Computer's score: {computer_score}. Your score: {user_score}"


def play_blackjack():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    game_over = False

    while not game_over:

        print(f"Your current card is {user_cards}. Your current score is {user_score}")
        print(f"Computer's first card is {computer_cards[0]}")
        if user_score > 21:
            game_over = True
        else:
            res = input(
                "Do you want to draw another card?(Type Y for Yes and N for No)\n> "
            ).lower()
            if res == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(computer_score, user_score))


while (
    input(
        "Do you want to play a BlackJack Game 🃏? (Reply Y for Yes and N for No)\n> "
    ).lower()
    == "y"
):
    os.system("cls")
    play_blackjack()
