from random import *
class Product:
    def __init__(self,name,count):
        self.name=name
        self.id=randrange(5000,6000)
        self.price=randrange(100,500)
        self.count=count

class Shop:
    stock={}
    def __init__(self):
        self.products=[]
        self.products_name=[]
    def add_to_cart(self,product):
        if product.name in self.products_name:
             self.stock[product.name]+=product.count
             print('Already exist')
        else:
            self.stock[product.name]=product.count
            self.products.append(product)
            self.products_name.append(product.name)
    def product_stock(self):
        for it in self.products:
            print(f'Name: {it.name}, Id: {it.id}, Price: {it.price}, Total Stock: {self.stock[it.name]}')
shop1=Shop()
while(True):
    op=int(input('Enter 1 for add an item in cart, 2 for stock, 3 for exit:'))
    if op==1:
        name=input('Enter name of the product:')
        count=int(input('Number of product:'))
        tmp=Product(name,count)
        shop1.add_to_cart(tmp)
    elif op==2:
        shop1.product_stock()
    elif op==3:
        break
    else:
        print('Invalid')