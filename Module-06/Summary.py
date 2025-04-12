class Book :
    def __init__(self,name):
        self.nama = name
    
    def read(self):
        raise NotImplementedError

class Math(Book):
    def __init__(self, name,lab):
        self.lab = lab
        super().__init__(name)

    def read(self):
        print('reading math')

shahin = Math('Shahin',True)
print(issubclass(Math,Book))
print(isinstance(shahin,Math))
print(isinstance(shahin,Book))

shahin.read()