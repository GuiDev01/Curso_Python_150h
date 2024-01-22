nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
#nome2 = nome.lower()
if not nome and not idade:
    print("Desculpe, você deixou ambos os campos vazios.")
else:
    nome2 = nome.lower()


    print(f'Seu nome é: {nome}')
    print(f'Nome invertido é {nome[::-1]}')
    print(f'Seu tem {len(nome2)}')
    if ' ' in nome2:
        print(f'Seu nome tem espaços:{nome2}')
    else:
        print('Seu nome não tem espaços')

    print(f'A primeira letra do seu nome é: {nome2[0]}')
    print(f'Sua ultima letra do nome é : {nome2[-1]}')
      






