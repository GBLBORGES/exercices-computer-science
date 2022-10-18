import locale

def calculute_discont_percent(fuel_type, fuel_liters):
    gasoline, alcohol = "G", "A"
    if (fuel_type == "G"):
        if fuel_liters < 20:
            discount_fuel_percent = fuel_liters - fuel_liters * 0.04
        else:
            discount_fuel_percent = fuel_liters - fuel_liters * 0.06
    elif (fuel_type == "A"):
        if fuel_liters < 20:
            discount_fuel_percent = fuel_liters - fuel_liters * 0.03
        else:
            discount_fuel_percent = fuel_liters - fuel_liters * 0.05
    else:
        return (f"fuel type {fuel_type} is wrong")

    return discount_fuel_percent


def calculate_value_fuel(fuel_type, fuel_liters):
    gasoline, alcohol = "G", "A"
    value_tobe_paid_gas, value_tobe_paid_alc = 2.5, 1.9
    discount_fuel = calculute_discont_percent(fuel_type, fuel_liters)
    total_value = 0
    if fuel_type == gasoline:
        total_value = discount_fuel * value_tobe_paid_gas
    elif fuel_type == alcohol:
        discount_fuel * value_tobe_paid_alc
    else:
        return "fuel type must G ou A"
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(round(total_value, 2))


print(calculate_value_fuel("G", 19.99))
