def sum_of_numbers(number):
    sum_of_values = 0
    counter = 1
    while counter <= number:
        sum_of_values += counter
        counter += 1
    return (sum_of_values)


print(sum_of_numbers(5))
