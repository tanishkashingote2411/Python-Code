import math

def calculate_area(shape, a, b=0):
    if shape == "circle":
        return math.pi * a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "triangle":
        return 0.5 * a * b

shape = input("Enter shape (circle/rectangle/triangle): ")

if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area =", calculate_area(shape, r))
else:
    a = float(input("Enter length/base: "))
    b = float(input("Enter breadth/height: "))
    print("Area =", calculate_area(shape, a, b))