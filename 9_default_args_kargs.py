#args syntax for java (int ... numbers)
def sum(*numbers):

    ans=0
    for number in numbers:
        ans+=number
    return ans


print(sum(45,46,47,48,49))