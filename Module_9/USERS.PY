from abc import ABC , abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []
        
    def add_driver(self,driver):
        self.drivers.append(driver)
        
    def add_rider(self,rider):
        self.riders.append(rider)   
        
    def __repr__(self) -> str:
        return (f'{self.company_name} with rider : {len(self.riders)} and driver : {len(self.drivers)}') 
    
class User(ABC):
    def __init__(self,name,gmail,nid) -> None:
        self.name = name
        self.gmail = gmail
        #TODO : set user id dynamically
        self.__id = 0
        self.nid = nid
        self.wallet = 0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, gmail, nid,current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, gmail, nid)
    
    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount
    
    def update_location(self,current_location):
        self.current_location = current_location
    
    def display_profile(self):
        print(f'the Rider name is: {self.name} and email is : {self.gmail}')
        
    def ride_request(self, ride_sharing, destination):
        if not self.current_ride:
            ride_request = Ride_Request(self,destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            self.current_ride = ride
            
    def show_current_ride(self):
        print(self.current_ride)
            
class Driver(User):
    def __init__(self, name, gmail, nid,current_location) -> None:
        super().__init__(name, gmail, nid)
        self.current_location = current_location
        self.wallet = 0
        
    def display_profile(self):
        print(f'driver with name : {self.name} and email is : {self.gmail}')
        
    def accept_ride(self,ride):
        ride.set_ride(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimate_fare = None
        
    def set_driver(self,driver):
        self.driver = driver
        
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self,rider,amount):
        self.end_time= datetime.now()
        self.rider.wallet -=self.estimate_fare
        self.driver.wallet +=self.estimate_fare
        
    def __repr__(self) -> str:
        return f'Ride details . From {self.start_location} to {self.end_location}'
    
class Ride_Request:
    def __init__(self,rider,end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        
class Ride_Matching:
    def __init__(self,driver) -> None:
        self.available_rider = driver
        
    def find_driver(self,ride_request):
        if len(self.available_rider)>0:
            driver = self.available_rider[0]
            ride = Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):
    speed ={
        'car' : 60,
        'bike' : 70,
        'cng' : 30,
        'noah' : 40 
    }
    
    def __init__(self,vehicle_type,vehicle_lisence,rate) -> None:
        self.vehicle_type = vehicle_type
        self.vehicle_lisence = vehicle_lisence
        self.rate = rate
        self.status = 'available'
        super().__init__()
        
    @abstractmethod
    def start_drive(self):
        pass
    
class Car(Vehicle):
    def __init__(self, vehicle_type, vehicle_lisence, rate) -> None:
        super().__init__(vehicle_type, vehicle_lisence, rate)
        
    def start_drive(self):
        self.status = 'unavailable'
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, vehicle_lisence, rate) -> None:
        super().__init__(vehicle_type, vehicle_lisence, rate)
    
    def start_drive(self):
        self.status = ' unavailable'
    
Pathao = Ride_Sharing("Pathao")
Jaber = Rider('Jaber','jaberriyan@gmail.com',12345,'moulvibazar',1300)
Pathao.add_rider(Jaber)
dola_pakhi = Driver('Dola Pakhi','dolapakhi@gmail.com',14567,'gulsan 1')
Pathao.add_driver(dola_pakhi)
Jaber.ride_request(Pathao,'chittagong')
Jaber.show_current_ride()