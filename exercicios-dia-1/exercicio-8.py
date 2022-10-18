def print_triangle(number):
    x = 1
    if number > 1:
        while x <= number:
            print(x * '*')
            x += 1
    else:
        'number must be greatter than 1'


print_triangle(5)
