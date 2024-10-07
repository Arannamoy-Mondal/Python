# encapsulation completed by mainly modifiers. it hides neccessary attribute from public.
import random
class bank:
    __balance=0
    def __init__(self,user_name,initial_deposit) -> None:
        self.user_name=user_name #public attribute
        self.user_id=random.randrange(1000,9999) # public attribute
        self.__balance=initial_deposit # private modifier declare by double underscore(__) in python
    def details(self):
        print(self.user_name,self.user_id,self.__balance)
    

ac1=bank('Hi',1000)
# print(ac1.__balance()) if you uncomment this line, this code give error because balance is a private attribute it can not accessed outside of the class
ac1.details()

#but private attribute can be accessed by dir
print(dir(ac1))
# if you see something like className__Attribute print(className__Attribute) 
print(ac1._bank__balance)
ac1._bank__balance+=1000
print(ac1._bank__balance)