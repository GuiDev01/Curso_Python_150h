pessoa = {}


chave = 'nome'

pessoa[chave] = 'Luiz Otavio'

pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'MARIA'

#del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')

else:
    print(pessoa['sobrenome'])