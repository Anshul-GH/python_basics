class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = 'Tonewood'

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print(f'This guitar has {self.numberOfStrings} strings. It is made of {self.typeOfWood} and it can play {self.numberOfMajorKeys} keys.')

if __name__ == "__main__":
    guitar = Guitar()
