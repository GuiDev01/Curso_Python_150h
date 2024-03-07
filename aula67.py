produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório',

}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'nome'
}

s1 = {2 ** i for i in range(10)}
print(s1)

