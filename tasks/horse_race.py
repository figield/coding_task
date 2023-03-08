import random


def run(horses):
    race_outcome = [(random.randint(0, power), power, name)
                    for name, power in horses.items()]

    race_outcome.sort(reverse=True)

    horse_order = [(name, power)
                   for _, power, name in race_outcome]

    return horse_order

