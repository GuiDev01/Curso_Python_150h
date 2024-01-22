


while True:
        
    try:

        numero1 = input('Digite um número para soma: ')
        numero2 = input('Digite um segundo número: ')
        operador = input('Digite o operador: ')
        nub1 = float(numero1)
        nub2 = float(numero2)

        if operador == '+':
            var = nub1 + nub2
        elif operador == '-':
            var = nub1 - nub2
        elif operador == '/':
            var = nub1 / nub2
        elif operador == '*':
            var = nub1 * nub2

        print('O Resultado de {} + {} é: {}'.format(nub1, nub2, var))


        continuar = input("Deseja fazer outra operação? (s/n): ")
        if continuar.lower() != 's':
            break  # Encerra o loop se o usuário não quiser continu

    except:
        print('erro')
        

        
    

    
        

    
    





