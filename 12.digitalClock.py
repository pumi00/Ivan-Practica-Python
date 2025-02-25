
def digital_clock(n):
    number_hours = n // 60
    number_minutes = n % 60
    return number_hours, number_minutes

print(digital_clock(213))