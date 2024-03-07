def calculo(numero):
    def nub (numero2):
        return numero * numero2
    return nub

conta = calculo(2)
conta2 = calculo(3)
conta3 = calculo(4)


var3 = input(' 2 para Duplicar: \n 3 para Triplicar: \n 4 para Quadruplicam: \n Digite:  ')

if var3 == '2':
    dois = int(input('Digite numero para duplicar: '))
    print(conta(dois))

elif var3 == '3':
    tres = int(input('Digite numero para Triplicar: '))
    print(conta2(tres))

elif var3 == '4':
    quard = int(input('Digite o numero para Qradruplicam: '))
    print(conta3(quard))
    
    

  
