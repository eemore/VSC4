class Shape:
    def area(self):
        #print("base clase area")
        self.calculate_area()

    def calculate_area(self):
        print("base clase CA")
        pass



    def show(self):
        self.show()

class Circle(Shape):
    pi = 3.14

    def __init__(self, redius):
        self.radius = redius

    def calculate_area(self):
        print("Area of circle :", self.pi * self.radius * self.radius)

    def show(self):
        print(f'Radius is {self.radius}')
        self.calculate_area()

class Rectangle(Shape):
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width



    def calculate_area(self):
        print("Area of Rectangle :", self.length * self.width)

    def show(self):
        print(f'Length={self.length}, Width={self.width}')
        self.calculate_area()

# function
def areaGF(shape):
    # call action
    shape.calculate_area()

# create object
#cir = Circle(5)
rect = Rectangle(10, 5)
rect2 = Rectangle()
# call common function
#areaGF(cir)
#areaGF(rect)

#cir.area()
#rect.area()
rect.show()
rect2.show()