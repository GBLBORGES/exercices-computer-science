def find_smaller_number(list_numbers):
    smaller_number = list_numbers[0]
    for number in list_numbers:
        if smaller_number > number:
            smaller_number = number
    return smaller_number


find_smaller_number([5, 9, 3, 19, 70, 8, 100, 2, 35, 27])
