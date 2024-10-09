#read only

class User:
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.money=money
    # getter
    @property # it convert method to attribute. it declares a method by default getter 
    def get_age(self): # it convert in to attribute because you use here property decorator
        print(f'Age: {self.age}')
    def get_money(self):
        print(f'Name: {self.name}, Age: {self.age}, Amount: {self.money}')
    
    # setter
    @get_age.setter # syntax for setter methodName.setter
    def get_age(self,value):
        self.age=value

user1=User('A',24,1000)
user1.get_age # attribute has no bracket but method has bracket
user1.get_money() # it's a method
user1.get_age=25
user1.get_age