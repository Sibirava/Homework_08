import random

VALUE1_DICE1 = 1
VALUE2_DICE1 = 6
VALUE1_DICE2 = 1
VALUE2_DICE2 = 6
NUMBER_TRIES = 10
def roll_dice():

    results = []
    count = 0
    for i in range(0, NUMBER_TRIES):
        dice1 = random.randint(VALUE1_DICE1, VALUE2_DICE1)
        dice2 = random.randint(VALUE1_DICE2, VALUE2_DICE2)
        if dice1 == dice2:
            count += 1
        results.append(dice1 + dice2)
    return (results, count)


def main():

    results, count = roll_dice()

    msg = f" In game there are such results {results}. Player won {count} time(s)"

    print(msg)

main()
