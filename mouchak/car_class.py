class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, number):

        self.mileage += number


    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"



blue = Car("blue", 20000)
red = Car("red", 30000)
print(f"{blue}\n{red}")

my_car = Car("black", 0)
print(my_car.mileage)
my_car.drive(100)
print(my_car.mileage)

