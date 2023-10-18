class Company:
    def __init__(self,name,address):
        self.name = name
        self.bus = []
        self.routes = []
        self.counter = []
        self.manager = []
        self.driver = []
        self.supervisors = []
        
class Driver:
    def __init__(self,name,lisence,age):
        self.name = name
        self.lisence = lisence
        self.age = age
        
class Supervisors:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
       
class Passengers:
    def __init__(self,name,start,end):
        self.name = name 
        self.start = start 
        self.end = end