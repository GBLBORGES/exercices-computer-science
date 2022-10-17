def find_triangle_type(side1, side2, side3):
    if ((side1 + side2) > side3 or side2 + side3 > side1 or side1 + side3 > side2):
        if (side1 == side2) and (side3 == side2):
            return ' Triângulo Equilátero: três lados iguais'
        elif (side1 == side2) or side3 == side2:
            return 'Triângulo Isósceles: quaisquer dois lados iguais'
        elif (side1 != side2) and side1 != side3 and side3 != side2:
            return 'Triângulo Escaleno: três lados diferentes'
    else:
        return ('it is not a triangle')


print(find_triangle_type(4, 5, 3))
