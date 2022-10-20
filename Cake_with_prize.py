# Cake with a surprise simulation

import random
prize1 = "GUM"
prize2 = "CANDY"
prize3 = "TOY_CAR"
prize4 = "ICE_CREAM"
prize5 = "AIR_BALOON"
prize6 = "TEDDY_BEAR"
prize7 = "CHOCOLATE_BAR"

def cake_with_prize():
    x = random.randint(0, 7)

    result = prize1
    if x == 1:
        result = prize2
    elif x == 2:
        result = prize3
    elif x == 3:
        result = prize4
    elif x == 4:
        result = prize5
    elif x == 5:
        result = prize6
    elif x == 6:
        result = prize7
    return result


def main():
    msg = f"Your prize is {cake_with_prize()}"
    print(msg)


main()
