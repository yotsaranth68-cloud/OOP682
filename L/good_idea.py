from abc import  abstractmethod
class Shape:
    @abstractmethod
    def resize(self, new_width, new_height): pass
        

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height
rect = Rectangle(2, 3)
print(resize_rectangle(rect, 4, 5))
square = Square(4)
print(resize_rectangle(square, 4, 5))