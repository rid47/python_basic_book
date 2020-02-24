class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod
    def welcomeMessage():
        print("Welcome to our orz")


employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()
