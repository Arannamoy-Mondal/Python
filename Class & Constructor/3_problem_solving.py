# make a simple calculator using class

class calc:
    def add(self,*num):
        sum=0
        for i in num:
            sum+=i
        print(sum)
    def multiplication(self,*num):
        ans=1
        for i in num:
            ans*=i
        print(ans)
    def divide(self,num1,num2):
        num1=int(num1)
        num2=int(num2)
        print(num1/num2)
    def subtraction(self,num1,num2):
        num1=int(num1)
        num2=int(num2)
        print(num1-num2)

calc1=calc()
calc1.add(5,6,7,8,9)
calc1.multiplication(1,2,3,4)
calc1.divide(10,2)
calc1.subtraction(10,3)