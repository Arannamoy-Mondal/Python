# make a class with n object
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __repr__(self):
        return(f'Name: {self.name}')
class Shop:
    def __init__(self,name):
        self.products=[]
        self.name=name
    def __repr__(self):
        return f'This shop name is {self.name}'
    def add_product(self,name,price):
        product=Product(name,price)
        self.products.append(product) 

shop1=Shop('Shop 1')
shop1.add_product('Iphone 15 pro max',1000)
shop1.add_product('Macbook M1',800)  
shop2=Shop('Shop 2')
shop2.add_product('Iphone 16 pro max',1600)
shop2.add_product('Macbook M3',3500)
print(shop1.products)
print(shop2.products)     