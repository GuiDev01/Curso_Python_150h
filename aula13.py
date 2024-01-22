nome = input('Escreva seu nome: ')
nome2 = len(nome)


if nome2 > 1:
    if nome2 <= 4:
        print('Seu nome é curto')
    elif nome2 >= 5 and nome2 <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite mais de mais letras')