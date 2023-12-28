import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def black_jack_game():
    """Take a list of cards and return the score calculated from the cards"""
    print(logo)
    players_choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
    if players_choice == 'n':
        exit()
    user_score = 0
    dealer_score = 0
    user = random.sample(cards, 2)
    dealer = random.sample(cards, 2)
    for user_card in user:
        user_score += user_card
    for dealer_card in dealer:
        dealer_score += dealer_card
    print(f"Your cards: {user}, current score: {user_score}\n")
    print(f"Dealer's first card: {dealer[0]}\n")
    add_card = 'n'
    while user_score <= 21:
        add_card = input("Type 'y' to get another card, type 'n' to pass:\n")
        if add_card == 'y':
          user.append(random.choice(cards))
          user_score = 0
          for user_card in user:
              user_score += user_card
          print(f"Your cards: {user}, current score: {user_score}\n")
          dealer.append(random.choice(cards))
          dealer_score = 0
          for dealer_card in dealer:
              dealer_score += dealer_card
          if dealer_score == 21:
              print("Lose, opponent has blackjack!\n")
              exit()
        else:
          if user_score <= 21:
              if user_score > dealer_score:
                print("You Win!")
              elif user_score == dealer_score:
                print("Its a Draw!\n")
              else:
                print("You Lose!\n")
          break
    else:
        print(f"Your final hand: {user}, final score: {user_score}\n")
        print(f"Dealer's final hand: {dealer}, final score: {dealer_score}\n")
        print("You went over, You Lose!\n")
    black_jack_game()
black_jack_game()
