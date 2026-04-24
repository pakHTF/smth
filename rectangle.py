class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return (self.height+self.width)*2
    def is_square(self):
        if self.height==self.width:
            return True
        else:
            return False
# primer
rect=Rectangle(3,7)
print(rect.area())        # 21
print(rect.perimeter())   # 20
print(rect.is_square())   # False
square=Rectangle(6,6)
print(square.is_square()) # True
