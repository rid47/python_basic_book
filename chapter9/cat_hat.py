cats = {}
for i in range(1, 101):
    cats["cat" + str(i)] = "no hat"

# print(cats)


round = 0
while True:
    for i in range(1, 101):
        if cats["cat" + str(i)] == "no hat":
            cats["cat" + str(i)] = "hat"
        else:
            cats["cat" + str(i)] = "no hat"
    round += 1
    if round == 100:
        print(cats)
        break

    for i in range(2, 101, 2):
        if cats["cat" + str(i)] == "no hat":
            cats["cat" + str(i)] = "hat"
        else:
            cats["cat" + str(i)] = "no hat"
    round += 1
    if round == 100:
        print(cats)
        break

    for i in range(3, 101, 3):
        if cats["cat" + str(i)] == "no hat":
            cats["cat" + str(i)] = "hat"
        else:
            cats["cat" + str(i)] = "no hat"
    round += 1
    if round == 100:
        print(cats)
        break
