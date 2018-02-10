import sys
import math

def errorHandler():
    print("Ожидается набор чисел")
    exit(1)


if sys.argv.__len__() != 4:
    errorHandler()


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


d = (b ^ 2) - (4 * a * c)
x1 = 0
x2 = 0

if d > 0:
    print("D > 0")
    sqrt_d = math.sqrt(d)
    _2a = 2 * a
    x1 = math.floor((-b - sqrt_d) / _2a)
    x2 = math.ceil((-b + sqrt_d) / _2a)
elif d == 0:
    print("D = 0")
    x1 = x2 = -(b/2*a)
else:
    print("D < 0")
    s = """
Корней на множестве действительных чисел нет.
А формулу комплексных корней не реализовал
    """
    print(s)
    exit(0)

print(f"x1 = {x1}, x2 = {x2}")

