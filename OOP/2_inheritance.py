from math import *
class shape:
    def __init__(self) -> None:
        pass
    def result(self):
        print('Area of:') 

class rectangle(shape):
    def __init__(self,width,length) -> None:
        self.width=width
        self.length=length
        super().__init__()
    def result(self):
        print('Area of rectange',self.length*self.width)

class circle(shape):
    def __init__(self,radius) -> None:
        self.radius=radius
        super().__init__()
    def result(self):
        print('Area of circle',pi*(self.radius**2))

class square(shape):
    def __init__(self,length) -> None:
        self.length=length
        super().__init__()
    def result(self):
        print('Area of square',self.length*self.length)
c1=circle(5)
c1.result()
r1=rectangle(5,6)
r1.result()
s1=square(5)
s1.result()

