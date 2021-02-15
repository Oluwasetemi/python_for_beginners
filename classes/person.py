class Person:
    """
    class person
    """

    def __init__(self, name) -> None:
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


temi = Person(name='temi')
temi.talk()
