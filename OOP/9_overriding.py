class human:
    def __init__(self,name):
        self.name=name
    def details(self):
        print('I am human')

class person(human):
    def __init__(self, name,age):
        self.age=age
        super().__init__(name)
    #override method
    def details(self):
        print('My name is',self.name)
    # + overload method
    def __add__(self,other):
        return(self.age+other.age)
    # > sign overload method
    def __gt__(self,other):
        return (self.age>other.age)

p1=person('Hello',24)
p2=person('Hi',36)
p1.details()
print(p1+p2)
print(p1>p2)