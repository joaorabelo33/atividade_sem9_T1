
def quadrado(lado_1, lado_2):
    if lado_1 == lado_2:
        print('QUADRADO')
    elif lado_1 != lado_2:
        perimetro= 2* lado_1 + 2 * lado_2
        area = lado_1 * lado_2
        
        print(f'{perimetro} - {area}')

lado_1= int(input())
lado_2= int(input())
resultado = quadrado(lado_1, lado_2)