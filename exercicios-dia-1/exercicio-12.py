def show_fatorial(number):
    x = 0
    fatorial = 1

    while x < number:
        x, fatorial = x + 1, fatorial * (x + 1)
    print(fatorial)


show_fatorial(6)
