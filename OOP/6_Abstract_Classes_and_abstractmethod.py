from abc import ABC,abstractmethod
#abstact base class
class animal(ABC):
    @abstractmethod #enforce all derived class to have this method
    def eat(self):
        # pass
        print('Animal eat')
    @abstractmethod #enforce all derived class to have this method
    def q_a(self):
        pass
        # print('Are you animal?')

class kangaroo(animal):
    def __init__(self,name) -> None:
        self.name=name
        super().__init__()

    def eat(self):
        print('I am',self.name)
    def q_a(self):
        pass # pass keyword used for skipping

k1=kangaroo('Kangaroo')
k1.eat()