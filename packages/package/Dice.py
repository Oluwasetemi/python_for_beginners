import random


class Dice:
    """
    a dice class
    """

    def roll(self):
        print('role a dice')
        random.seed()
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        output = first, second
        return output


dice1 = Dice()
res = dice1.roll()
print(res)
