class Animal:
    def __init__(self, name, color, age):

        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.color} and {self.age} old"

    def sound(self, sound):
        return f"{self.name} makes {sound} sound"


class Cow(Animal):
    def sound(self, sound="moo moo"):
        return super().sound(sound)


class Chicken(Animal):
    def sound(self, sound="cheep cheep"):
        return super().sound(sound)


class Goat(Animal):
    def sound(self, sound="bleat bleat"):
        return super().sound(sound)


my_cow = Cow("max", "red", "4 years")
my_chicken = Chicken("timothy", "white", "1 week")
my_goat = Chicken("tom", "white", "2 years")

print(my_cow)
print(my_cow.sound())

print(my_chicken)
print(my_chicken.sound())

print(my_goat)
print(my_goat.sound())
