import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_hand(cards):
    """It take a card list as a parameter, and calculate the hand score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score, computer_score):
    """Determines game result by calculating scores."""
    if user_score == computer_score:
        return "Draw 🤝"
    elif computer_score == 0:
        return "You lose, opponent has BlackJack ☠️"
    elif user_score == 0:
        return "You win with Blackjack 🎉"
    elif user_score > 21:
        return "You went over. You lose 😣"
    elif computer_score > 21:
        return "Opponent went over. You win 🥸"
    elif user_score > computer_score:
        return "You win 🤩"
    else:
        return "You lose 💀"

def core_game():
    """It start the core game loop."""
    user_hand = []
    computer_hand = []
    game_over = False

    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while game_over == False:
        user_score = calculate_hand(user_hand)
        computer_score = calculate_hand(computer_hand)
        print(f"Your cards: {user_hand}, Your score: {user_score} ")
        print(f"Opponnent first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_deal == "y":
                user_hand.append(deal_card())

            else:
                game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = calculate_hand(computer_hand)

    print("====================================================")
    print(f"Your cards: {user_hand}, Your score: {user_score} ")
    print(f"Opponent cards: {computer_hand}, Opponent score: {computer_score} ")
    print(compare_score(user_score, computer_score))