"""
Interpolação básica de stings
%s - strigs
%d %e %i int
%f float
x% e X% Hexadecimal(ABCDEF0123456789)
"""




nome = 'Gui'
preco = 1000.95897643
variavel = '%s, o preço é R$%f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500,1500))