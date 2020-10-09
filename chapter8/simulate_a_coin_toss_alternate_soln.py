import random


def single_trial():
    flip_result = random.randint(0, 1)
    flip_count = 1

    while flip_result == random.randint(0, 1):
        flip_count += 1

    flip_count = flip_count + 1
    return flip_count


def flip_trial_avg(num_trials):
    total = 0
    for trial in num_trials:
        total = total + single_trial()

    return total/num_trials


print(f"The avg number of coin flips was {flip_trial_avg(10_000)}")
