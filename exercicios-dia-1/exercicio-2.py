def arithmetic_mean(number_list):
    total_number = 0
    for number in number_list:
        total_number += number
    return total_number/len(number_list)


print(arithmetic_mean([5, 10, 10, 5, 5]))
