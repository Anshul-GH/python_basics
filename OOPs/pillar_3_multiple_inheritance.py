class OperatingSystem:
    multitasking = True
    name = 'Mac OS'

class Apple:
    website = 'www.apple.com'
    name = 'Apple'

class MacBook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking is True:
            print(f'This is a multitasking system. Visit {self.website} for more details.')
            print('Name: ', self.name)


if __name__ == "__main__":
    macBook = MacBook()