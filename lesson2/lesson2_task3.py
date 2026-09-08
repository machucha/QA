import math


def square(a):
    return math.ceil(a * a)


a = float(input("Длинна стороны - "))
result = square(a)
print(result)
