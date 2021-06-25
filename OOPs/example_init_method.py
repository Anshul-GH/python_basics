class Employee:
    def __init__(self, name):
        self.name = name

    # def enterEmployeeDetails(self):
    #     self.name = "Mark"

    def displayEmployeeDetails(self):
        print(self.name)


if __name__ == "__main__":
    employee = Employee("Mark")
    employee.displayEmployeeDetails()

    employee2 = Employee("Matthew")
    employee2.displayEmployeeDetails()
