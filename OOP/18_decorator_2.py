# passing value in decorator
from math import *
def timer(work):
    def iner(n):
        print('Inner start')
        work(n)
        print('Inner end')
    return iner
@timer
def get_fact(n):
    print('Get Fact function executed')
    print(f'Factorial of {n} = {factorial(n)}')

get_fact(5)