class shop:
    cart=[] # class attribute
    def __init__(self,seller) -> None:
        self.seller=seller
    def add_to_cart(self,item):
        self.cart.append(item)



a=shop('A')
a.add_to_cart('HP')
a.add_to_cart('Lenovo')
a.add_to_cart('Acer')
print(a.cart)