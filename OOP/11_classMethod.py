class Shopping:
    def __init__(self,itemName,price):
        self.itemName=itemName
        self.price=price
    
    @classmethod
    def details(self,name,price):
        print(f'Item Name: {name}, Price: {price}')

Shopping.details('Laptop',350)

        