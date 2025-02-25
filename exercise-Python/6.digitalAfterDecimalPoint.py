import math

def first_digits(num):

    return int(str(math.floor(num*10)/10)[-1])

print(first_digits(2.6))