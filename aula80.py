from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print(' ')

pessoa = [
    'joão', 'Joana', 'Luiz', 'Leticia',
]


camisetas = [
    ['preta', 'branca'],
    ['m', 'p', 'g'],
    ['Femenina', 'Masculina', 'unisex'],
    ['algodão','poliéster'],

]


#print_iter(combinations(pessoa, 2))
#print_iter(permutations(pessoa, 2))
print_iter(product(*camisetas))



