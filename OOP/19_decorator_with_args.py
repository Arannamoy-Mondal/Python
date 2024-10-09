from math import *
from time import *
def timer(work):
    def inner(*args,**kwargs):
        print('Inner function start')
        start=time()
        work(*args,**kwargs)
        print('Inner function end')
        end=time()
        print(-start+end)
    return inner

@timer
def sum(args):
    print('Sum function executed')
    print(f'Factorial of {factorial(args)}')

sum(1200)
