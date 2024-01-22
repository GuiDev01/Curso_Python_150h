numero = input('Digite um Número: ')

try: 
    numero2 = int(numero)
    if numero2 % 2 == 0 :
    
        print(f'Número é par: {numero}')
    else:
        print(f'Número é impar: {numero}')
except:
    print('Você não digitou um número inteiro')
