class cal:
    def __init__(self,a) -> None:# this method is called  dunder method
        self.a=a
    def __add__(self,other) -> None:# this method is called  dunder method
        return self.a+other.a
    def __mul__(self,other) -> None:# this method is called  dunder method
        return self.a*other.a
    
cal1=cal(5)
cal2=cal(6)
print(cal1+cal2)
print(cal1*cal2)