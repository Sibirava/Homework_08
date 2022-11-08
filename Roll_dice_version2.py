import random


def throw_bones(num_bones):
    sum_points = 0
    throw_list = ""
    for i in range(num_bones):
        throw = random.randint(1, 6)
        throw_list += f"{throw} "
        sum_points += throw
    return f"{sum_points}, dropped out:{throw_list}"


def main():
    you_score = throw_bones(2)
    print(f"The sum of your points: {you_score}")
    opponents_score = throw_bones(2)
    print(f"Opponent's score: {opponents_score}")

    if you_score > opponents_score:
        msg = f"You won!!!"
    elif opponents_score > you_score:
        msg = f"You lose..."
    else:
        msg = f"Draw"

    print(msg)

main()
