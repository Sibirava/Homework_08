#Simple poker
import random

def form_card_deck():
    pokers = []
    poker = []
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    playing_card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Lady", "King", "Ace"]

    for i in suits:
        for j in playing_card:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
    return pokers

def difine_table(pokers):

    table = []

    card = random.randrange(pokers)
    table.append(card)
    return table


def main():
    pokers = form_card_deck()

    #player_number = int(input("Input player number: "))

    table = difine_table(pokers)

    print(table)

main()
