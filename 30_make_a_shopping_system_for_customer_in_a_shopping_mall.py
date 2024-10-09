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
    def buy_product(self,name,number):
        if name in self.products_name and self.stock[name]>=number:
            print('Congratulations you have successfully bought this product')
            self.stock[name]-=number
        else:
            print('Not Available')
shop1=Shop()
while(True):
    op=int(input('Enter 1 for add an item in cart, 2 for buy product, 3 for exit:'))
    if op==1:
        name=input('Enter name of the product:')
        count=int(input('Number of product:'))
        if(type(name)==str and type(count)==int):
               tmp=Product(name,count)
               shop1.add_to_cart(tmp)
               shop1.product_stock()
    elif op==2:
        product=input('Enter product name:')
        number=int(input('Enter number of product'))
        if(type(name)==str and type(count)==int):
                shop1.buy_product(product,number)
                shop1.product_stock()
    elif op==3:
        break
    else:
        print('Invalid')