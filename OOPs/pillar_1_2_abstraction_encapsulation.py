# Class => Library
# Layers of abstraction => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book

class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print('Available Books:')
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print('You have borrowed the book: ', requestedBook)
            self.availableBooks.remove(requestedBook)
        else:
            print('Sorry the book is not available.')

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned the book. Thank you!')


class Customer:
    def requestABook(self):
        print("Enter the name of the book you want: ")
        self.book = input()
        return self.book

    def returnABook(self):
        print('Enter the name of the book you want to return:')
        self.book = input()
        return self.book

if __name__ == "__main__":
    library = Library(['Think and grow rich', 'Who will cry when you die', 'For one more day'])
    customer = Customer()
    while True:
        print()
        print('Choose one option:')
        print('1 -> Display the available books.')
        print('2 -> Request for a book.')
        print('3 -> Return a book.')
        print('0 -> Exit.')

        userInput = int(input())

        if userInput == 1:
            library.displayAvailableBooks()
        elif userInput == 2:
            requestedBook = customer.requestABook()
            library.lendBook(requestedBook)
        elif userInput == 3:
            returnBook = customer.returnABook()
            library.addBook(returnBook)
        else:
            quit()
    