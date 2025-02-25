
def total_cost(d,c, n):

    total_cents = (d * 100 + c) * n
    total_dolars = total_cents // 100
    remianing_cents = total_cents % 100

    return total_dolars, remianing_cents