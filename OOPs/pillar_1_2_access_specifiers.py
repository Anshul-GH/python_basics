# public, private, protected

# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car:
    numberOfWheels = 4
    _color = 'Black'
    __yearOfManufacture = 2017 # _Car__yearOfManufacture -> Concept is called name mangling

class Bmw(Car):
    def __init__(self):
        print('Protected Attribute _color: ', self._color)

if __name__ == "__main__":
    car = Car()
    print('Public Attribute numberOfWheels: ', car.numberOfWheels)
    
    bmw = Bmw()

    print('Private Attribute __yearOfManufacture: ', car._Car__yearOfManufacture)
