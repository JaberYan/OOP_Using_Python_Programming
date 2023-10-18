class Pen:
    def __init__(self,brand,color,head_size,head_color):
        self.brand = brand
        self.color = color
        self.head_size = head_size
        self.head_color = head_color
        
        
First_pen = Pen('matador','red','90px','white')
print(First_pen.brand,First_pen.color,First_pen.head_size,First_pen.head_color)