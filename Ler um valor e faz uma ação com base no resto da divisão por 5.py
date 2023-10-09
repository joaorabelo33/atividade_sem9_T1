

def divisao_5(n):
    div = n % 5 
    if div == 0:
        print(f'{9 * n+ 7 }')
    elif div == 1:
        if n % 2 == 0:
            print('par')
        elif n % 2 != 0:
            print('ímpar')
    elif div == 2:
        print(f'{(5 * ( n * n)) - (3 * n) + 42 }')
    elif div == 3:
        print(f'{n // 10}')
    elif div == 4:
        print(f'{n ** 2}')
n=int(input())
resultado=divisao_5(n)