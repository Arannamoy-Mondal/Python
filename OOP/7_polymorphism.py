# for more information search on google
from math import*
class shape:
    def __init__(self,name) -> None:
        self.name=name
    def area():
        print('Area:')

class rectangle(shape):
    def __init__(self, name,width,length) -> None:
        self.width=width
        self.length=length
        super().__init__(name)
    def __repr__(self) -> str:
        return f'Rectangle Area: {self.length*self.width}'

class circle(shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)
    def __repr__(self) -> str:
        return f'Circle Area: {pi*(self.radius**2)}'

r1=rectangle('Rectangle_1',50,60)
c1=circle('Circle_1',50)
print(r1)
print(c1)