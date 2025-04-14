class CPU:
    def __init__(self,cores):
        self.cores = cores

class RAM:
    def __init__(self,size):
        self.size = size

class HardDrive:
    def __init__(self,capacity):
        self.capcity = capacity

# Computer "has a" CPU
# Computer "has a" RAM
# Computer "has a" Hard Drive
class Computer: 
    def __init__(self,cores,memorySize, hardDiskCapacity):
        self.cpu = CPU(cores)
        self.ram = RAM(memorySize)
        self.hardDisk = HardDrive(hardDiskCapacity)