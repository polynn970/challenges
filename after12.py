import math

class Apple:
    def _init_(self,t,c,m,w):
        self.taste = t
        self.color = c
        self.mold = 0
        self.weight = w

class Circle:
    def __init__(self,l,w):
        self.len = l
        self.width = w
        
    def area(self):
        return self.len * self.width * math.pi

class Triangle:
    def __init__(self,y,n):
        self.yoko = y
        self.naname = n
        
    def area(self):
        return self.yoko * self.naname / 2

class Hexagon:
    def __init__(self,leng):
        self.leng = leng

    def calculate_perimeter(self):
        return self.leng * 6
    
circle = Circle(3,3)
print(circle.area())

triangle = Triangle(5,5)
print(triangle.area())

hexagon = Hexagon(10)
print(hexagon.calculate_perimeter())

    

