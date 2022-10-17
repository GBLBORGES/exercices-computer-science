def bigger_length(list_names):
    bigger_name = 'x'
    for name in list_names:
        if len(name) > len(bigger_name):
            bigger_name = name
    return bigger_name


print(bigger_length(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
