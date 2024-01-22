"""
funções:
split divide uma string
join une uma string
strip corta os espaços da frente e atras de uma frase

"""

frase = '   Olha só que, coisa interessante    '  
lista_palavras = frase.split(', ')
lista_frases_sem_nada = []


for i, frase in enumerate(lista_palavras):
     lista_frases_sem_nada.append(lista_palavras[i].strip())


#print(lista_frases_sem_nada)
     
frase_unidas = '__'.join(lista_frases_sem_nada)
print(frase_unidas)