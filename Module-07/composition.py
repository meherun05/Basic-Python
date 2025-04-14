class Engine:
    def __init__(self):
        pass

    def start(self):
        print('engine starting..')

class Driver:
    def __init__(self):
        pass

#Car "has a" engine 
class Car:
    def __init__(self):
        self.engine = Engine()
        self.driver = Driver()

    def carStart(self):
        self.engine.start()