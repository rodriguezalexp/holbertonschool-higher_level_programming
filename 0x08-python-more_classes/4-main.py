#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(4, 8)

print(str(my_rectangle))
print(repr(my_rectangle))
print(my_rectangle.area(), my_rectangle.perimeter())
print(repr(Rectangle))
Rectangle.height = 23
print(Rectangle.__dict__)
del(my_rectangle)

