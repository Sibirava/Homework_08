# Cake with a surprise simulation

import random
NUMBER_TRIES = 5

def cake_with_prize():
    prizes = ["GUM", "CANDY", "TOY_CAR","ICE_CREAM", "AIR_BALLOON", "TEDDY_BEAR", "CHOCOLATE_BAR"]
    results = []

    for i in range(0, NUMBER_TRIES):
        result = random.choice(prizes)
        results.append(result)
    return results
def main():
    msg = f"Your prize is {cake_with_prize()}"
    print(msg)


main()
