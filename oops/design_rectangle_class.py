"""


Exercise 6: Design a Rectangle class with default attributes for length and width set to 1.
Include methods to set these attributes and calculate the area.
"""


class Rectangle:

    def __init__(self, length:int=1, width:int=1) -> None:
        self._length = length
        self._width = width

    def set_length(self, length: int) -> None:
        self._length = length

    def set_width(self, width) -> None:
        self._width = width

    def area(self) -> int:
        return self._length * self._width


rect  = Rectangle()
print(rect.area())
# setting lenght and width
rect.set_length(10)
rect.set_width(15)
print(rect.area())
