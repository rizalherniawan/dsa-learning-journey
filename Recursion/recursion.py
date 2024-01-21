def exponential(n,x):
    if x == 0: return 1
    else: return n * exponential(n, x - 1)

def factorial(n):
    if n == 1 or n == 0: return 1
    else: return  n * factorial(n - 1)


# print(exponential(4,2))

print(factorial(4))