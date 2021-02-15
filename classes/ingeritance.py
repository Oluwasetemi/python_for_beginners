class Mamal:
    """
    mamal class
    """
    def walk():
        print('can walk')


class Dog(Mamal):
    """
    docstring
    """
    def bark():
        print('only a dog can bark')


dog = Dog
dog.walk()
dog.bark()
