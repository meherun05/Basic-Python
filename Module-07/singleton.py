#singleton = one single instance
# if we want a new instance, we will get the  old one (already created )instance

class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This singleton already have a instance please use that by calling getInstance()')
    
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    
first = Singleton.getInstance()
second = Singleton.getInstance()
third = Singleton.getInstance()
print(first)
print(second)
print(third)

last = Singleton()