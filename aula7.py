"""
try/except
try - > tentar executar o código
exept -> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobra o número que vc digitar: ')



try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float )
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('isso não é um numero')
