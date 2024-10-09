class Engine:
    def __init__(self):
        pass
    def start(self):
        print('Engine started')

class Bus: # bus has an engine 

    def __init__(self):
        self.engine=Engine()
    # @classmethod
    def start(self):
        self.engine.start()

Bus1=Bus()
Bus1.start()
