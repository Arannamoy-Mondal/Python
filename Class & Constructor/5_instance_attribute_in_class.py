class shop:
    def __init__(self,buyer) -> None:
        self.buyer=buyer
        self.cart=[] #intance attribute

    def add_to_cart(self,item):
        self.cart.append(item)


a=shop('A')
a.add_to_cart('CPU')
a.add_to_cart('GPU')
a.add_to_cart('PSU')
a.add_to_cart('RAM')
print(a.cart)
b=shop('B')
b.add_to_cart('Acer')
b.add_to_cart('HP')
b.add_to_cart('Lenovo')
print(b.cart)