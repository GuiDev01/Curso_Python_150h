nome = 'luiz Otávio'
adicionar = '*'

i = 0 


nova_str = ""

while i < len(nome) -1:
    nova_str += nome[i] + adicionar
    i += 1


nova_str = nova_str + nome[i]
 

print(nova_str)



