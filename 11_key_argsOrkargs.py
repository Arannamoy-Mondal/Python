# def full_name(first,last):
#     return (f'{first} {last}')
# print(full_name('Hello','World'))



def full_name(first,last, **str):
    ans=''
    for key,value in str.items():
        ans+=value
        ans+=' '
    return ans

print(full_name(first='Hello',last='Hi',last1='Bye',first1='Bye',last2='Bye'))

