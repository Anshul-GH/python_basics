from abc import ABCMeta, abstractmethod


class Shape(metaclass = ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print('Area of square is: ', self.side * self.side)

class Rectangle(Shape):
    width = 4
    height = 10
    def area(self):
        print('Area of rectangle is: ', self.width * self.height)


if __name__ == "__main__":
    square = Square()
    square.area()

    rectangle = Rectangle()
    rectangle.area()
