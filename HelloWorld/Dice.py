import random

class Dice:
    def roll_on(self):
        v1 = random.randint(1, 6)
        v2 = random.randint(1, 6)
        return v1, v2

