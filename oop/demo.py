class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('Mizan', 2)
s2 = Student('Jenny', 3)
print(s1.lap.brand)
