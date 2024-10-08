quantity={}
class Product:
    def __init__(self,name,id,price,count):
        self.name=name
        self.id=id
        self.price=price
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
s1=Shop()
p1=Product('Banana',234,15,10)
p2=Product('Apple',235,20,10)
p3=Product('Tomatoo',236,5,10)
p4=Product('Tomatoo',236,5,20)
p5=Product('Banana',234,15,100)
s1.add_to_cart(p1)
s1.add_to_cart(p2)
s1.add_to_cart(p3)
s1.add_to_cart(p4)
s1.add_to_cart(p5)
s1.product_stock()