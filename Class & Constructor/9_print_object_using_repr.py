class shop:
    def __init__(self,buyer,item,price,quantity) -> None:
        self.buyer=buyer
        self.item=item
        self.price=price
        self.quantity=quantity
    def __repr__(self) -> str:
        return f'Name: {self.buyer}, Product name: {self.item}, Price: {self.price}, Quantity: {self.quantity}'
    
hello=shop('Dan Mishal','Threadripper 3990x','2000$',1)
print(hello)
