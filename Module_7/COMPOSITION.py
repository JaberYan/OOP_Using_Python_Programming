class Engine:
    def __init__(self) -> None:
        pass
    
    def start(self):
        print('engine started')
    
class driver:
    def __init__(self) -> None:
        pass
        
class car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = driver