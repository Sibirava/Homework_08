import random

def form_card_deck():
    card_deck = []
    card = []

    for i in ['Heart', 'Spade', 'Diamond', 'Club']:
        for j in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            card.append(i)
            card.append(j)
            card_deck.append(card)
            card = []
    return card_deck

def form_table_cards(card_deck):
    table = []

    for card in range(0, 5):
        card = random.choice(card_deck)
        table.append(card)
        card_deck.remove(card)
    return table

def form_player_cards(card_deck,amount_players):

    player_cards = []

    for i in range(0, amount_players):
        for card in range(0, 2):
            card = random.choice(card_deck)
            player_cards.append(card)
            card_deck.remove(card)
    return player_cards

def main():
    amount_players = int(input("Input the amount of players: "))
    card_deck = form_card_deck()

    table = form_table_cards(card_deck)
    player_cards = form_player_cards(card_deck, amount_players)

    msg = f"Table cards: {table} \n" \
          f"players_cards: {player_cards}"

    print(msg)


main()
