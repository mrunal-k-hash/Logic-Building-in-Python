"""
# wap to check number is prime or not using a function
def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number.")
else:
    if prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")"""

# wap to reverse any no using a function
"""def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev"""


# wap to calculate factorial of a number using a function
"""def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter a number: "))
print("Factorial of", num, "is", fact(num))"""


# wap to calculate addition of 2 , 3 or n nos or list using a function
"""
def add(a, b):
    return a + b


# main
x = 10
y = 20
x = 30
l = 40
m = 50
print("addition of x and y =", add(x, y))
print("addition of x and y z l and m = ", add(add(add(x, y), l), m))
L1 = [1, 2, 3, 4, 5]
sum = 0
for ele in L1:
    sum = add(sum, ele)
    print("addition of list elements = ", sum)"""


# wap to calculate square root

"""num = float(input("enter a number: "))
sr = num**0.5
print("square root of given number is ", sr)"""

# help of math module
import math

num = float(input("enter a number: "))
sr = math.sqrt(num)
print("square root of given number is ", sr)
