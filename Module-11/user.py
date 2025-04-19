from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,email,nid):
        super().__init__()
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    
    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError