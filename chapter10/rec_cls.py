class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"length: {self.length} and width: {self.width}"


class Square(Rectangle):
    def __init__(self, side_lenght):
        super().__init__(side_lenght, side_lenght)


my_sqr = Square(4)

print(my_sqr)
print(my_sqr.area())
