def factorial(val: int):
    if val <= 1:
        return 1
    return val * factorial(val-1)


print (factorial(5))


def fibbonaci(n):
    if n<=1:
        return n
    return fibbonaci(n-1) + fibbonaci(n-2)

