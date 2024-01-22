hora = input('Digite a hora: ')

try:
    hora2 = int(hora)

    if hora2 > 0 and hora2 < 11:
        print('Bom dia')

    elif hora2 >= 12 and hora2 <= 17:
        print('Boa tarde')

    elif hora2 >= 18 and hora2 <= 23:
        print('Boa noite')

except:
    print('Por favor, digite apenas número inteiros')


