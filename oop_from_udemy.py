class Employee:
    # name = "Ben"
    working_hours = 40
    designation = "Sales Executive"
    seles_made_this_week = 6

    def HasAchievedTarget(self):
        if self.seles_made_this_week >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")


employee_one = Employee()
employee_two = Employee()
# print(employee_one.name)
# employee_one.HasAchievedTarget()
# print(employee_one.working_hours)
# Employee.working_hours = 45
# print(employee_one.working_hours)
employee_one.name = "John"
employee_two.name = "Mary"
