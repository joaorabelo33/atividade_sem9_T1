


def calcular(valor_1,valor_2, operacao):
    if operacao == 1:
        adicao= valor_1 + valor_2
        print(f'{adicao}')
    elif operacao == 2:
        subtracao=valor_1 - valor_2
        print(f'{subtracao}')
    elif operacao == 3:
        multi= valor_1 * valor_2
        print(f'{multi}')
    elif operacao == 4:
        divi=valor_1 / valor_2
        print(f'{divi:.2f}')
    else:
        print('Operação inválida!')

valor_1=int(input())
valor_2=int(input())
operacao=int(input())
resultado=calcular(valor_1, valor_2,operacao)