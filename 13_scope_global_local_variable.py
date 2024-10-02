sum=5000

def minus():
    global sum # for accessing global variable in python used global keyword
    sum-=500
minus()
print(sum)