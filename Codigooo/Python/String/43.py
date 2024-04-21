from math import pi

def rectangle_area(length, width):
    return length*width

def cylinder_volume(r, height):
    return pi*r*r*height

print('The area of the rectangle is %.2f cm\u00B2' % rectangle_area(5.5, 7))
print('The volume of the cylinder is %.2f cm\u00B3' % cylinder_volume(5.5, 7))