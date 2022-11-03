import random
AMOUNT_PLAYERS = 5

def form_table_cards(suits, cards_value):

    table = []

    for card in range(0, 2):
        card = random.choice(suits), random.choice(cards_value)
        table.append(card)
    return table

def form_player_cards(suits, cards_value):

    player_cards = []

    for player in range(1, AMOUNT_PLAYERS):
        for card in range(0, 4):
            card = random.choice(suits), random.choice(cards_value)
            player_cards.append(card)
    return player_cards


def main():
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    cards_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Lady", "King", "Ace"]

    table = form_table_cards(suits, cards_value)
    players = form_player_cards(suits, cards_value)

    msg = f"Poker game started \n " \
          f"table cards are: {table}\n" \
          f"Player's cards are {players}"
    print(msg)

main()

