import random


def unfair_trail(param):
    if random.random() < param:
        return "A"
    else:
        return "B"


win_count = 0

for trail in range(10_000):
    region_won = 0

    if unfair_trail(.87) == "A":
        region_won += 1
    if unfair_trail(.65) == "A":
        region_won += 1
    if unfair_trail(.17) == "A":
        region_won += 1
    if region_won >= 2:
        # print("Candidate A wins!")
        win_count += 1


percentage = (win_count/10_000) * 100

print(f"percentage of where Candidate A wins: {percentage}")
