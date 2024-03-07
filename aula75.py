def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(d):
    tipo_n = type(d)
    if not isinstance(d, (float, int)):
        raise TypeError(
            f'{d} deve ser int ou float'
            f' "{tipo_n.__name__}" enviado'
        )

    

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    
    nao_aceito_zero(d)
    return n / d

print(divide(2 ,'0'))