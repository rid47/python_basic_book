import random


def roll():
    return random.randint(1, 6)


sum = 0
for trail in range(10_000):
    sum = sum + roll()


avg = sum / 10_000

print(f"avg number rolled: {avg}")
