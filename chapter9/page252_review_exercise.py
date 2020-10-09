food = ["rice", "beans"]
print(food)
food.append("broccoli")
print(food)
food.extend(["bread", "pizza"])
print(food)
print(f"{food[0]} , {food[1]}")
print(food[-1])

breakfast_str = "eggs, fruit, orange juice"
breakfast = breakfast_str.split(", ")
print(len(breakfast))
