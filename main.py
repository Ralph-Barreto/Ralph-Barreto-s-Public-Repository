#Setting up all the necessary variables, lists, dictionaries and functions which will be sued throughout.
import art
import random
cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
playing = True
picture_cards = {
    "Ace" : [1, 11],
    "Jack" : 10,
    "Queen": 10,
    "King": 10
}

def draw_card(hand):
    """ Draws a card for a player. """
    card = random.choice(cards)
    hand.append(card)

def sum_of_hand(hand):
    """ Calculates the sum of the values in a given hand without altering the names of the original hand. """
    temp_hand = []
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            temp_hand.append(picture_cards[card])
        elif card == "Ace":
            temp_hand.append(picture_cards["Ace"][1])
        else:
            temp_hand.append(card)
        if sum(temp_hand) > 21:
            index = 0
            for card_check in hand:
                if card_check == "Ace":
                    temp_hand[index] = picture_cards["Ace"][0]
                index += 1
    return sum(temp_hand)

#The game begins
while playing:
    start_up = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    start_up = start_up.lower()

    # This draws 2 cards for both the computer and player. Then it outputs one card for the computer's hand and both cards for the player.
    if start_up == "y":
        game_over = False
        print("\n" * 100 + art.logo)
        computer_hand = []
        player_hand = []

        for draw in range (0,2):
            draw_card(computer_hand)
            draw_card(player_hand)
        print(f" The computer's first card is: {computer_hand[0]}")

        # This allows the player to draw another card. Then it checks if their hand is below 21, if so it will repeat until the player decides against drawing another card, or they go over 21.
        while not game_over:
            print(f" Your cards are: {player_hand}")

            while sum_of_hand(computer_hand) < 17:
                draw_card(computer_hand)

            if sum_of_hand(player_hand) > 21:
                game_over = True
            else:
                another_card = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
                if another_card == "y":
                    draw_card(player_hand)
                else:
                    game_over = True

        # Displays both hands and then checks to see who has won the game and states the result.
        print(f"    Your final hand: {player_hand}")
        print(f"    Computer's final hand: {computer_hand}")

        if sum_of_hand(player_hand) > 21:
            winner = False
            print("You went over.")
        elif sum_of_hand(computer_hand) > 21:
            winner = True
            print("The computer went over.")
        elif sum_of_hand(player_hand) > sum_of_hand(computer_hand):
            winner = True
            print("Your hand is higher than the Computer's.")
        elif sum_of_hand(player_hand) < sum_of_hand(computer_hand):
            winner = False
            print("Your hand was weaker than the Computer's.")
        else:
            winner = False

        if sum_of_hand(computer_hand) == sum_of_hand(player_hand):
            print("Both of your hands are equal. It is a draw.")
        elif winner :
            print("You Win!")
        else:
            print("You Lose!")

    else:
        playing = False
