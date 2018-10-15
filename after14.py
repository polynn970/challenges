class Square:
    square_list = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.square_list.append((self.x, self.y))

    def print_size(self):
        print("{} by {}".format(self.x,self.y))

s1 = Square(20,30)
s2 = Square(30,40)
s3 = Square(50,30)

print(s1.print_size())

print(Square.square_list)

class Ika:
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y
    """
    def compe(x,y):
        return print(x is y)

surume = Square
tako = Ika

print(Ika.compe(surume,tako))
