class Shape:
    def __init__(self,s):
        self.sen = s

    def what_am_i(self):
            print("I am a Hero..." + self.sen)

class Rectangle(Shape):
    """
    def __init__(self,l,q):
        self.len = l
        self.quan = q
    """
    def calculate_perimeter(self):
        return self.len * 3

class Square(Shape):
    """
    def __init__(self,l,q):
        self.len = l
        self.quan = q
    """
    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self):
        return self.len + 1

shape = Shape("Zoff")
print(shape.what_am_i())
"""
rec = Rectangle(5,3)
print(rec.calculate_perimeter())

sq = Square(4,4)
print(sq.calculate_perimeter())

print(sq.change_size())
print(sq.change_size())
"""
recs = Rectangle("mekabu")
print(recs.what_am_i())


class Horse:
    def __init__(self,p,r):
        self.pet = p
        self.rider = r

class Rider:
    def __init__(self,n):
        self.name = n

rider = Rider("箱根駅伝")
horse = Horse("aoyama",rider)
print(horse.rider.name)
