from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triagle


print("Circle")
radius_1=Circle(5)
print("Square", radius_1.getSquare())
print("Perimetrer", radius_1.getPerimeter())

#Circle
#Square 15.707963267948966
#Perimetrer 31.41592653589793

print("-----------------------------------")

print("Square")
side_1=Square(5)
print("Square", side_1.getSquare())
print("Perimetrer", side_1.getPerimeter())

#Square
#Square 25
#Perimetrer 10

print("-----------------------------------")

print("Rectangle")
with_height_1=Rectangle(5, 6)
print("Square", with_height_1.getSquare())
print("Perimetrer", with_height_1.getPerimeter())

#Rectangle
#Square 30
#Perimetrer 11

print("-----------------------------------")

print("Triagle")
values=Triagle(2, 1, 2, 3)

print("Square", values.getSquare())
print("Perimetrer", values.getPerimeter())

#Triagle
#Square 0.5
#Perimetrer 6