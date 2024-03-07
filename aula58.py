p1 = {
    'nome': 'Luiz',
    'sobrenome' : 'Miranda'

}

#print(p1.get('nome', 'nome não existe'))

#nome = p1.pop('nome')
#print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

#p1.update(nome='Novo valor', idade=30)
#print(p1)

tupla = (('nome', 'novo valor'), ('idade', 30))

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)

