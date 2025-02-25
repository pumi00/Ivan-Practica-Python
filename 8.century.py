import math

def century(num):
    if num % 100 == 0:
        return math.floor(num / 100)
    else:
        return math.floor(num / 100 +1)