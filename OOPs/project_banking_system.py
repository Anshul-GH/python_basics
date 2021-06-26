## My Solution ##

# from random import randint

# class Account:
#     def __init__(self, name, deposit):
#         self.name = name
#         self.deposit = deposit
#         self.account_number = randint(10000, 99999)
#         print(f'Your assigned account # is: {self.account_number}')

#     def display_acct_details(self):
#         print(f'Hi {self.name}! Your account #{self.account_number} has balance amount of ${self.deposit}.')


# if __name__ == "__main__":
#     account = Account('Mark', '20000')    
#     account.display_acct_details()

## My Solution Ends ##

from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}
    
    def createAccount(self, name, deposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, deposit]
        print("Account has been created successfully. Your account number is: ", self.accountNumber)
    
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print('Authentication Successful')
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print('Insufficient balance.')
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            # print('Withdrawal was successful. Available balance: ', self.savingsAccounts[self.accountNumber][1])
            print('Withdrawal was successful.')
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print('Deposit was successful.')
        self.displayBalance()

    def displayBalance(self):
        print("Available Balance: ", self.savingsAccounts[self.accountNumber][1])


if __name__ == "__main__":
    savingsAccount = SavingsAccount()
    while True:
        print('Choose an option:')
        print('1 -> Create an account.')
        print('2 -> Access existing account.')
        print('0 -> Exit.')

        userChoice = int(input())

        if userChoice == 1:
            print('Enter your name: ')
            name = input()
            print('Enter the initial deposit: ')
            deposit = int(input())

            savingsAccount.createAccount(name, deposit)

        elif userChoice == 2:
            print('Enter your name: ')
            name = input()
            print('Enter your account number: ')
            accountNumber = int(input())

            authenticationStatus = savingsAccount.authenticate(name, accountNumber)
            if authenticationStatus:
                while True:
                    print('Choose an option:')
                    print('1 -> Withdraw.')
                    print('2 -> Deposit.')
                    print('3 -> Display available balance.')
                    print('0 -> Go back to previous menu.')

                    userChoice = int(input())

                    if userChoice == 1:
                        print('Enter a withdrawal amount:')
                        withdrawalAmount = int(input())
                        savingsAccount.withdraw(withdrawalAmount)
                    
                    elif userChoice == 2:
                        print('Enter a deposit amount:')
                        depositAmount = int(input())
                        savingsAccount.deposit(depositAmount)

                    elif userChoice == 3:
                        savingsAccount.displayBalance()

                    else: #if userChoice == 0:
                        break
        
        else: #if userChoice == 3:
            quit()
