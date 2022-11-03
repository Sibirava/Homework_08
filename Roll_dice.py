import random

VALUE1_DICE1 = 1
VALUE2_DICE1 = 6
VALUE1_DICE2 = 1
VALUE2_DICE2 = 6
COUNT = 100
def roll_dice():

    num_simulations = 0

    while num_simulations <= COUNT:
        dice1 = random.randint(VALUE1_DICE1, VALUE2_DICE1)
        dice2 = random.randint(VALUE1_DICE2, VALUE2_DICE2)
        num_simulations += 1
        print(dice1, dice2)
        if dice1 == dice2:
            msg = f"You won with sum {dice1 + dice2}"
        else:
            msg = f"{dice1 + dice2} Casino wins"
        return msg


def main():

  game = roll_dice()
  print(game)

main()
