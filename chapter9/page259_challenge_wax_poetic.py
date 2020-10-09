Nouns= ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
Verbs= ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
Adjectives= ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
Prepositions= ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
Adverbs= ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]

import random

choosen_nouns = []
choosen_verbs = []
choosen_adjectives = []
choosen_prepositions = []
choosen_adverbs = []


for i in range(3):
    choosen_nouns.append(random.choice(Nouns))
    choosen_verbs.append(random.choice(Verbs))
    choosen_adjectives.append(random.choice(Adjectives))
    choosen_prepositions.append(random.choice(Prepositions))


choosen_adverbs.append(random.choice(Adverbs))


# print(choosen_adjectives[0][0])

# print(f"A {choosen_adjectives[0]} {choosen_nouns[0]}\n")
# print(f"A {choosen_adjectives[0]} {choosen_nouns[0]} {choosen_verbs[0]} {choosen_prepositions[0]} the {choosen_adjectives[1]} {choosen_nouns[1]}\n")
# print(f"{choosen_adverbs[0]}, the {choosen_nouns[0]}{ choosen_verbs[1]}\n")

# print(f"the {choosen_nouns[1]} {choosen_verbs[2]} {choosen_prepositions[1]}  a {choosen_adjectives[2]} {choosen_nouns[2]}\n")


if "aeiou".find(choosen_adjectives[0][0]) != -1:
    article = "An"
else:
    article = "A"


poem = (
    f"{article} {choosen_adjectives[0]} {choosen_nouns[0]}\n\n"
    f"{article} {choosen_adjectives[0]} {choosen_nouns[0]} {choosen_verbs[0]} {choosen_prepositions[0]} the {choosen_adjectives[1]} {choosen_nouns[1]}\n"
    f"{choosen_adverbs[0]}, the {choosen_nouns[0]} {choosen_verbs[1]} \n"
    f"the {choosen_nouns[1]} {choosen_verbs[2]} {choosen_prepositions[1]} a {choosen_adjectives[2]} { choosen_nouns[2]}"

    )


print(poem)
