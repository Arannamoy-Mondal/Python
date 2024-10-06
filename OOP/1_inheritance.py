class creature:
    def __init__(self,name) -> None:
        self.name=name
    def details(self):
        print('I am',self.name)


class human(creature):
    def __init__(self, name) -> None:
        super().__init__(name)
    def details(self):
        print('Hello, we are human.My name is',self.name)


class animal(creature):
    def __init__(self, name) -> None:
        super().__init__(name)
    def details(self):
        print('We are animal. I am from',self.name)
    
man=human('Python')
man.details()
elephant=animal('Thailand')
elephant.details()
lion=animal('South Africa')
lion.details()
kangaroo=animal('Australia')
kangaroo.details()
dog=animal('German, Shephard')
dog.details()

