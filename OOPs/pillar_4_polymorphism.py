# the operator looks the same but behaves differently depending on the input.
# Example: Addition (+ operator)
# number + number = sum
# string + string = concatenation

# Overriding

class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
    
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()


if __name__ == "__main__":
    employee = Employee()
    employee.setNumberOfWorkingHours()
    print('Number of working hours of employee: ', end='')
    employee.displayNumberOfWorkingHours()

    trainee = Trainee()
    trainee.setNumberOfWorkingHours()
    print('Number of working hours of trainee: ', end='')
    trainee.displayNumberOfWorkingHours()
    trainee.resetNumberOfWorkingHours()
    print('Number of working hours of trainee after reset: ', end='')
    trainee.displayNumberOfWorkingHours()
