def digit_sum(num):
    aux = 0
    for x in str(num):
        aux = aux + int(x)
    return aux