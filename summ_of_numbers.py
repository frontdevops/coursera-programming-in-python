
import sys


def errorHandler():
    print("Нужно передать аргумент из цифр")
    exit(1)


if sys.argv.__len__() < 2:
    errorHandler()

digit_string = sys.argv[1]

if not digit_string.isdigit():
    errorHandler()


n = 0
for i in digit_string:
    n += int(i)

print(n)

