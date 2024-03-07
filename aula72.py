def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

def gen2(gen):
    yield from gen()
    yield 5
    yield 6
    yield 7
    yield 8


g = gen2(gen1)
for n in g:
    print(n)



