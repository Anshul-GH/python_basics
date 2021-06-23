class Employee:
    def employeeDetails(self):
        self.name = 'Matthew'
        print("Name: ", self.name)
        self.age = 30
        print("Age: ", self.age)

    def printEmployeeDetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


if __name__ == "__main__":
    employee = Employee()
    employee.employeeDetails()
    # Employee.employeeDetails(employee)
    employee.printEmployeeDetails()
