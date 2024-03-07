x, y, *resto = 1, 2, 3, 4, 
print(x, y, resto)


def soma (*args):
    total = 0
    for numero in args:
        total += numero
        
    return total


    

nub = 1, 2, 3, 4, 5, 6, 7, 8, 9 

soma_1_2_3 = soma(*nub)

print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)

print(soma_4_5_6)

print(sum(nub))

