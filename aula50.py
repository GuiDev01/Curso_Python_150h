def saucacao (msg, nome):
    return f'{msg}, {nome}!'


def executar (funcao, *args):
    return funcao(*args)


v = executar(saucacao, 'Bom dia', 'Guilherme')
print(v)