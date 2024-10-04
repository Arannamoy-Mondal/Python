class laptop:
    def __init__(self,brand,cpu,gpu,ram):
        self.brand=brand
        self.cpu=cpu
        self.gpu=gpu
        self.ram=ram
    


laptop1=laptop('Lenovo','Ryzen 7 5825u','Radeon','16gb')
print(laptop1.brand)
print(laptop1.cpu)
print(laptop1.gpu)
print(laptop1.ram)
        