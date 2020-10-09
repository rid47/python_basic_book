class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Length: {self.length} & Width: {self.width}"



class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)



my_square  = Square(4)
print(my_square.area())


