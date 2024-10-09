def time():
    def inner():
        print('Inner start')

        print('Inner end')
    return inner

# time()
time()() # this is called decorator