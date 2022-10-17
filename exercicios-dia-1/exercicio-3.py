def print_asterisks(number):
    x = 0
    if number > 1:
        while x < number:
            x += 1
            print(number * "*")
    else:
        print('number must be greater than 1')


print_asterisks(4)
