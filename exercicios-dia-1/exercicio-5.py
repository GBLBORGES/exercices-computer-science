def calculate_value_per_m2(m2):
    cans_paint, value_total = round(m2/54), (round(m2/54)) * 80

    return (cans_paint, value_total)


print(calculate_value_per_m2(2000))
