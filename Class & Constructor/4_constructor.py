class laptop:
    # def __init__(self) -> None:
    #     pass
    # above two line use for declare a constructor in python
    def __init__(self,brand,cpu,ram) -> None:
        self.brand=brand
        self.cpu=cpu
        self.ram=ram

    def details(self):
        res=f'{self.brand} \n{self.cpu}\n{self.ram}'
        print(res)

laptop1=laptop('HP','Ryzen 5 5625u','16 gb')
laptop1.details()
