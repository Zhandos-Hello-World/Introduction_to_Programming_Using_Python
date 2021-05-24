import math as m

radius = eval(input("Enter the radius and length of a cylinder: "))
length = eval(input())
area = radius * radius * m.pi
volume = area * length
print('The area is', area)
print('The volume is', volume)
