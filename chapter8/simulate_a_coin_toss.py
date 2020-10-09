import random


def flip_coin():

    """Flip Coin"""
    number = random.randint(0, 1)

    if number == 1:
        return "heads"
    else:
        return "tails"


result = []
sum = 0

def required_flip():

    while(True):
        r = flip_coin()
        if len(result) == 0:
            result.append(r)
        elif r in result:
            result.append(r)
        else:
            result.append(r)
            return len(result)


for trial in range(10_000):
    sum = sum + required_flip()
    result.clear()


print(f"avg flip per trial: {int(sum/10000)}")
