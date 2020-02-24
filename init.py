class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


employee = Employee("Ridwan")
employee2 = Employee("Rashed")
employee.display()
employee2.display()
