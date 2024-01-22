
import os 

var2 = 'perfume'
letras_acertadas = ''
qtd_acertos = 0


while True:
    qtd_acertos += 1

    var = input('Digite uma letra: ')
    if len(var) > 1:
        print('Digite apenas uma letra!!!!!')
        continue
    
    if var in var2:
        letras_acertadas += var

    palavra_formada = ''

    for letra_secreta in var2:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            

  
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == var2:
        os.system('cls')
        print(f'Você acertou a palavra: {palavra_formada} ')
        print(f'Foram {qtd_acertos} de tentativas')
        break
    


    
        

  
        

        




