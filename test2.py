class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added: {product}")

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                if product.stock > 0:
                    product.stock -= 1
                    print(f"Successfully bought {product.name}.Stock: {product.stock}")
                    print("Congress message: Thank you for your purchase!")
                    return
                else:
                    print(f"Sorry, {product.name} is out of stock.")
                    return
        print(f"Product {product_name} not found in the shop.")


# Example usage
if __name__ == "__main__":
    shop = Shop()
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 10)
    product3=Product("Tablet",1000,10)
    product4=Product("Tablet",1000,10)
    shop.add_product(product1)
    shop.add_product(product2)
    shop.add_product(product3)
    shop.add_product(product4)
    shop.buy_product("Laptop")      # Should successfully buy
    shop.buy_product("Smartphone")   # Should show out of stock
    shop.buy_product("Tablet")       # Should show not found
