class Shopping:
    cart=[] # static attribute
    origin='China' # static attribute
    def __init__(self,location,name):
        self.location='Jamuna' # instance attribute
        self.name='Jamuna'
    def purchase(self,item,price,amount):
        remaining=amount-price
        print(f'Buying: {item} for price {price} and remainin {remaining}')
    @classmethod # using classmethod you can access this method declaring without any class
    def purchase2(self,item):
        print(f'Buying {item}')


Shopping.purchase('Laptop',2,1200,350)
Shopping.purchase2('Laptop')