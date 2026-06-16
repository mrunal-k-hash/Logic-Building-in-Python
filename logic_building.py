# wap to calculate square root (exponentiation operator)

"""num = float(input("enter a number: "))
sr = num**0.5
print("square root of given number is ", sr)"""

# help of math module
"""import math

num = float(input("enter a number: "))
sr = math.sqrt(num)
print("square root of given number is ", sr)"""

# wap to calculate area if triangle

"""height = float(input("enter height of triangle: "))
base = float(input("enter base of triangle:"))
area = (1 / 2) * base * height
print("area of triangle is ", area)"""


# variable swapping using third variable

"""x = float(input("enter a number: "))
y = float(input("enter another number: "))
print(x)
print(y)
z = x
print("value of z afer swapping is ", z)

x = y
print("value of x after swapping is ", x)

y = z
print("value of y after swapping is", y)"""

# variable swapping without using third variable

"""x = float(input("enter a number: "))
y = float(input("enter another number: "))
print(x)
print(y)
x, y = y, x
print("value of x ", x)
print("value of y", y)"""


# wap to convert km to m
"""km = float(input("enter distance in km : "))
m = km * 1000
print(km, "km will be  ", m, "m")"""

# wap to check whether a number is positive, negative or zero
num = float(input("enter a number: "))
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")
