
import re 
import sys


cpf3 = input('Digite seu cpf: ')
cpf = re.sub(
    r'[^0-9]',
    '',
    cpf3
)

entrada_e_sequecial = cpf == cpf[0] * len(cpf)  

if entrada_e_sequecial:
    print('Você mandou números iguais!!!')
    sys.exit()


var = cpf[:9]
n = 10
soma = 0



    
for i in var:
    soma += int(i) * n
    n -= 1 
digito_1 = (soma * 10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 

dez_digitos = var + str(digito_1)
n_2 = 11


soma_2 = 0 

for i in dez_digitos:
    soma_2 += int(i) * n_2
    n_2 -= 1 
digito_2 = (soma_2 * 10 ) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0 

cpf_gerado_pelo_calculo = f'{var}{digito_1}{digito_2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf3} é válido')
else:
    print('CPF inválido')









    

