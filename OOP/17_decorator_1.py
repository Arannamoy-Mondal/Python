def timer(work):
    def inner_fun():
        print('Inner start')
        work()
        print('Inner end')
    return inner_fun

@timer # it's called decorator. it's a nested function which take parameter
def get_work():
    print('Work function execute')

get_work()