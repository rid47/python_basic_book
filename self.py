class Employee:
    def employeeDetails(self):
        self.name = "Mizan"
        print("Name = ", self.name)
        self.age = 30
        print("Age = ", self.age)

    def printEmployeeDetails(self):
        print("Printing in another details")
        print("Name: ", self.name)
        print("Age: ", self.age)


employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
