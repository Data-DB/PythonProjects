import random
from art import logo
print(logo)
# Creating a indexed list
deck_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "K", "Q", "J"]
# Assigning value to elements from deck_list using dictionary
dict_deck = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,"8": 8, "9": 9, "10": 10, "A": 11, "K": 10, "Q": 10, "J": 10}
print("Welcome to black jack!")
# Use lists to store cards for player and computer
player_cards = []
computer_cards = []
not_enough = True

# Draw a card method


def hit(list):
    """Used to draw a card from the deck"""
    return random.choice(list)

# Used to calculate score for player, takes input from player_cards list


def user_score(card_list):
    """Used to keep track of the players score"""
    # Store math operations
    add_score = []
    not_ace = []
    sum_of_not_ace = 0
    # Determins if a card is an A
    for card in card_list:
        if card != 'A':
            not_ace.append(dict_deck[card])
            sum_of_not_ace = sum(not_ace)
    # Determines if the ace value shold be 1 or 11
    for card in card_list:
        if card == 'A':
            if (sum_of_not_ace + dict_deck[card]) <= 21:
                add_score.append(dict_deck[card])
            elif (sum_of_not_ace + dict_deck[card]) > 21:
                add_score.append(dict_deck['A'] - 10)
        else:
            add_score.append(dict_deck[card])
    return sum(add_score)

# Used to calculate the computers score, takes input from computer_cards list. Same as user_score with methods used to calc score


def house_score(card_list):
    """Used to keep track of the dealer score"""
    add_score = []
    not_ace = []
    sum_of_not_ace = 0

    for card in card_list:
        if card != 'A':
            not_ace.append(dict_deck[card])
            sum_of_not_ace = sum(not_ace)
    for card in card_list:
        if card == 'A':
            if (sum_of_not_ace + dict_deck[card]) <= 21:
                add_score.append(dict_deck[card])
            elif (sum_of_not_ace + dict_deck[card]) > 21:
                add_score.append(dict_deck['A'] - 10)
        else:
            add_score.append(dict_deck[card])
    return sum(add_score)


if input("Would you like to play a round? Type 'y' or 'n': ") == 'y':
    # setting parameters to determine gameplay
    stay = True
    bust = False
    hit_me = 'h'

    # player score
    score = 0
    # computer score
    dealers_score = 0

    # Draw a card for computer
    dealer_card_1 = hit(list=deck_list)
    # Take drawn card put in computer card list
    computer_cards.append(dealer_card_1)
    # display computer_cards
    for comp_card in computer_cards:
        print(f"dealer has {comp_card}")
    dealers_score = house_score(card_list=computer_cards)

    # Player draw card display score
    player_card_1 = hit(list=deck_list)
    player_cards.append(player_card_1)
    for player_card in player_cards:
        print(f"player has {player_card}")
    score = user_score(card_list=player_cards)
    print(f"Player score is: {score}")

    # Used for the player to draw cards or stay
    while bust != True and hit_me != 's':  # player
        hit_me = input("Would you like to Hit (h) or Stay (s)?: ").lower()
        if hit_me == 'h':
            hits = hit(list=deck_list)
            print(f"Next card is: {hits}")
            player_cards.append(hits)
            print("player has a: ")
            for player_card in player_cards:
                print(player_card)
            score = user_score(card_list=player_cards)
            print(f"Player score is: {score}")
            if score > 21:
                bust = True
        elif score == 21:
            hit_me = 's'

    while not_enough != False and bust != True:  # computer
        if score >= 22:
            bust = True
        # computer stays if its score is higher than players
        elif dealers_score > score:
            not_enough = False
        # Displays dealer score.
        elif dealers_score <= 16:
            hits_D = hit(list=deck_list)
            computer_cards.append(hits_D)
            for comp_card in computer_cards:
                print(comp_card)
            dealers_score = house_score(card_list=computer_cards)
            print(f"Dealer score is: {dealers_score}")
       # Makes computer stay if score is between 17 and 21
        elif dealers_score >= 17 and dealers_score < 21:
            not_enough = False
        elif dealers_score > 21:
            bust = True

# Conditions used to evaluate who is the winner
if dealers_score >= 22:
    print("Player wins!")
elif score >= 22:
    print("Dealer wins!")
elif dealers_score == score:
    print("It's a tie!")
elif dealers_score < score:
    print("Player wins!")
elif score > dealers_score:
    print("Plays wins!")
elif dealers_score > score:
    print("Dealer wins!")
else:
    print("Thanks for playing!")
