class Star_Cinema:
    hall_list = []
    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)
        

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        for row in range(1,rows+1):
            self._seats[row] = [0]*cols
            
        Star_Cinema.entry_hall(self)
        
    def entry_show(self,id,movie_name,time):
        movie= (id,movie_name,time)
        self._show_list.append(movie)
        self._seats[id] = [[0] * self._cols for _ in range(self._rows)]
        
    def book_seats(self,id,row,col,owner):
        try:
            show_seats=self._seats[id]
        except KeyError:
            print("Invalid show ID.")
            return

        if 1<=row<=self._rows and 1<=col<=self._cols:
            if show_seats[row-1][col-1]==0:
                show_seats[row-1][col-1]=1
                print("--------------------------")
                print(owner,"your booked successfully and seat :",'(',row,',',col,') for id :',id,' this show')
                print("--------------------------")
            else:
                print("-----------------------")
                print("Seat is already booked.")
                print("-----------------------")
        else:
            print("-------------------------")
            print("Invalid seat coordinates.")
            print("-------------------------")
        
        
    def view_show_list(self):
        return (self._show_list)
    
    def view_available_seats(self, show_id):
        try:
            show_seats = self._seats[show_id]
            available_seats = [(row + 1, col + 1) 
                               for row in range(self._rows) 
                                    for col in range(self._cols) 
                                        if show_seats[row][col] == 0]
            return available_seats

        except KeyError:
            raise TypeError ("Invalid Show ID")


movie = Hall(5,5,1)
movie.entry_show('1','JAWAN','9:00 AM')
movie.entry_show('2','PATHAN','2:00 PM')
movie.entry_show('3','DUNKI','6:00PM')
while True:
    print("1.VIEW ALL SHOW TODAY")
    print("2.VIEW AVAILABLE SEATS")
    print("3.BOOK TICKET")
    print("EXIT")
    option = int(input("ENTER OPTION : "))
    if(option==1):
        print("------------------------------------------------------------------------------------------------------------------")
        print("MOVIE ID : MOVIE NAME : TIME : ",movie.view_show_list())
        print("------------------------------------------------------------------------------------------------------------------")
    elif(option==2):
        show_id = str(input("ENTER ID : "))
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        print("SEAT : ",movie.view_available_seats(show_id))
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
    elif(option==3):
        id = input("ENTER ID : ")
        ticket = int(input("NUMBER OF TICKET :"))
        owner = input("ENTER OWNER NAME : ")
        for i in range(1,ticket+1):
            ROW = int(input("ENTER ROW : "))
            COL = int(input("ENTER COL : "))
            movie.book_seats(id,ROW,COL,owner)
    else:
        break
    