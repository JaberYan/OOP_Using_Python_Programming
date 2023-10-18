class Orderr:
    def __init__(self,customer,itmes) -> None:
        self.customer = customer
        self.items = itmes
        total = 0
        for item in itmes:
            total +=item.price
        self.bill = total    
        