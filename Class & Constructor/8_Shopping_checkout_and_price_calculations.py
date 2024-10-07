class shop:
    def __init__(self) -> None:
        self.cart=[]
    def add_to_cart(self,item,quantity,price):
        self.cart.append({'item':item,'quantity':quantity,'price':price})
    def details(self):
        total=0
        for i in self.cart:
            print(f'Item: {i['item']}, Price: {i['price']}$, Quantity: {i['quantity']}$')
            total+=int(i['price']*i['quantity'])
        print(f'Total price {total} $')


hello=shop()
hello.add_to_cart('Ryzen 5 3600',10,100)
hello.add_to_cart('Ryzen 9 3950x',10,490)
hello.add_to_cart('i9 14900k',10,625)
hello.details()