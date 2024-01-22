"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [20, 30, 40, 50]
lista.append('aa')
var = lista.pop()
lista.append(1231)
del  lista[-1]
# limpa a lista 
# lista.clear()
lista.insert(0, 1234)

print(lista, 'removido', var)