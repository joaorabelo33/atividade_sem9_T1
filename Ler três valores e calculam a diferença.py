
def qual_menor(numero_dois, numero_tres, numero_um):
    if(abs(numero_dois - numero_um) <= abs(numero_tres - numero_um)):
        return numero_dois - numero_um
    elif(abs(numero_dois - numero_um) >= abs(numero_tres - numero_um)):
        return numero_tres - numero_um
    else:
        raise ValueError('entrada inválida')
def main(): 
    numero_um = input().strip() 
    numero_dois = input().strip()
    numero_tres = input().strip()

    numero_um = int(numero_um)
    numero_dois = int(numero_dois)
    numero_tres = int(numero_tres)

    resultado = qual_menor(numero_dois, numero_tres, numero_um)


    print(f'{abs(resultado)}')


if __name__=='__main__':
    main()