import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterado = iter(iterable)

lista = [n for n in  range(10000)]

generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))

for n in generator:
    print(n)