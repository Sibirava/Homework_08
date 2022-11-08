import random

suits = ["spades", "clubs", "diamonds", "hearts"]
ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

deck = [r + " " + s for r in ranks for s in suits] #создаем колоду карт


def discard_card(deck, num_cards):
    result = ""
    for i in range(num_cards):
        card = random.choice(deck) #выбрасываем карту из колоды
        deck.remove(card) #удаляем ее из колоды, чтобы не повторялась
        result += f"{card}\n" #результат получаем с помощью конкотенации строк
    return result


def main():
    num_players = int(input(f"Input number of players: "))

    for i in range(num_players):
        print(f"Player сards #{i + 1}:")
        print(discard_card(deck, 2))

    print(f"5 cards per table:")
    print(discard_card(deck, 5))


main()