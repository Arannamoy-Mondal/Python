class Shop:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    @staticmethod # If you declare staticmethod in any method, you can access this method without declaring any instance attribute
    def multiply(a,b):
        print(a*b)



Shop.multiply(20,40)