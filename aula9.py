condicão = True
passou_no_if = None

if condicão:
    passou_no_if = True
    print('Faça algo')

else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if ')
else:
    print('Passou no if')