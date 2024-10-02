def total(*numbers):
    ans=0
    multi=1
    for number in numbers:
        ans+=number
        multi*=number
    return ans,multi