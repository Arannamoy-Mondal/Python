# Search on google
from time import *
class Watch:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def details(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Time: {time()}')

class FitnessTracker:
      def __init__(self,price,step):
           self.price=price
           self.step=step
        #    super().__init__(brand, model)
class SmartWatch(Watch,FitnessTracker):
     def __init__(self, brand, model,price,step):
          Watch.__init__(self,brand,model)
          FitnessTracker.__init__(self,price,step)
     def details(self):
          print(f'Branf: {self.brand}, Model: {self.model}, Time: {time()}, Step: {self.step}')

Watch1=Watch('Casio','I don''t know')
FitnessTracker1=FitnessTracker(8000,750)
SmartWatch1=SmartWatch('Honor','GS3',8000,750)
Watch1.details()

