class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age,coat_color):
        self.name= name
        self.age= age
        self.coat_color = coat_color

    def __str__(self):
            return f"{self.name} is {self.age} years old"

    def speak(self,sound):
            return f"{self.name} barks: {sound}"
        


class Jack(Dog):
    def speak(self,sound="Arf"):
        #return f"{self.name} says {sound}"
        return super().speak(sound)
class Dach(Dog):
    pass
class Bulldog(Dog):
    pass
