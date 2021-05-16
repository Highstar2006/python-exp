##

# 1 function with 1 parameter to tell me time of city
# 1 function with 1 parameter to tell me day in city
import datetime


def timeofCity():
    return datetime.datetime.now()


print(timeofCity())


# 4functions with 2 parameters,add,subtract,mutipity,divde.

def addnumber(a, b):
    sum = a + b
    return sum


num1 = 12
num2 = 8
print(addnumber(num1, num2))


def subract(c, d):
    sub = c - d
    return sub


num3 = 12
num4 = 8
print(subract(num3, num4))


def multiply(e, f):
    times = e * f
    return times


num5 = 12
num6 = 8
print(multiply(num5, num6))


def divide(g, h):
    times = g / h
    return times


num7 = 12
num8 = 8
print(divide(num7, num8))
