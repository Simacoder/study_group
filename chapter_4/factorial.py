# Factorial function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # n is 5 then factorial is 5 -1 = 4, repeat this until n = 0

print(factorial(5))