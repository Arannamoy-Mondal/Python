# function is a first class object
def hybrid_arch():
    print('P core + E core')
    def inner_fun():
        print('inside the inner')
        return f'300$'
    return inner_fun

hybrid_arch()
# print(hybrid_arch())
print(hybrid_arch()())
