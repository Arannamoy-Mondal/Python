class laptop:
    brand='Lenovo'
    cpu='Ryzen 5 5600H'
    ram='16 gb'
    def details(self): #for creating method in must use a parameter
        print(self.brand,self.cpu,self.ram)
    def price(self):
        text=f'Current price is {500}$'
        print(text)
laptop1=laptop()
laptop1.details()
laptop1.price()