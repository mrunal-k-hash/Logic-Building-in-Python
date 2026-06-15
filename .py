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
        print(num, "is not a prime number.")
