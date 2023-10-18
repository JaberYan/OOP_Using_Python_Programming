class CPU:
    def __init__(self,cores) -> None:
        self.core = cores
        
class RAM:
    def __init__(self,size) -> None:
        self.size = size
        
class HardWare:
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        
class Computer:
    def __init__(self,cores,size,capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.HDW = HardWare(capacity)
        
    def __repr__(self) -> str:
        print(f'computer cpu is {self.cpu} cores and ram size is of our computer {self.ram} and lastly hardware capacity is our computer {self.HDW}')
        
jaber = Computer(7,'8 GB','1 TB')
print(jaber.cpu,jaber.ram,jaber.HDW)