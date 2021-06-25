# single inheritance
class Apple:
    manufacturer = 'Apple Inc.'
    contactWebsite = 'www.apple.com/contact'

    def contactDetails(self):
        print('To contact us, log on to: ', self.contactWebsite)

# single inheritance: Base Class -> Apple, Derived Class -> MacBook
class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufacturerDetails(self):
        print(f'This MacBook was manufactured in the year {self.yearOfManufacture} by {self.manufacturer}')

if __name__ == "__main__":
    macBook = MacBook()
    macBook.manufacturerDetails()
    macBook.contactDetails()
