class Employee:
    numberOfWorkingHours = 40
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved!")
        else:
            print("Target has not been achieved.")


if __name__ == "__main__":
    employeeOne = Employee()
    # employeeOne.hasAchievedTarget()
    # print(employeeOne.name)
    print(employeeOne.numberOfWorkingHours)

    employeeTwo = Employee()
    # print(employeeTwo.name)
    print(employeeTwo.numberOfWorkingHours)

    ## Class Attribute ##
    # Change the value of the attribute globally
    Employee.numberOfWorkingHours = 45

    # The value will be changed now
    print(employeeOne.numberOfWorkingHours)
    print(employeeTwo.numberOfWorkingHours)


    ## Instance Attribute ##
    # Create an instance attribute with the
    # same name and override the value
    employeeOne.numberOfWorkingHours = 40

    # The value will be changed now
    print(employeeOne.numberOfWorkingHours)
    print(employeeTwo.numberOfWorkingHours)
