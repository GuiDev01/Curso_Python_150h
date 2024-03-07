a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',

}


#(a1, a2), (b1, b2) = pessoa.items()

##print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

#pessoa_completa ={**pessoa, **dados_pessoa}
#print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq=12334)