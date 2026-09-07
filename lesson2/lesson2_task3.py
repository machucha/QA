import math


def square(a):
    return math.ceil(a * a)


sum = float(input("Длинна стороны - "))
result = square(sum)
print(result)
