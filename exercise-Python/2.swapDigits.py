
def swap_digits(number):
    aux = str(number)[1], str(number)[0]
    return int(aux)

print(swap_digits(30))
