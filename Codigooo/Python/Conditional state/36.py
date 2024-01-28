#Write a Python program to check if a triangle is equilateral, isosceles or scalene.
#Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with (at least) two equal sides.

x=int(input("Side A "))
y=int(input("Side b "))
z=int(input("Side c "))

if (x==y==z):
    print("Triangle is equilateral ")
elif(x!=y==z):
    print("Triangle is isoceles ")
else:
    print("Triangle is scalane ")
    
    