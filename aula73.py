try:


    a = 18
    b = 0
    c = a / b
    print('linha 2' [2222])

except ZeroDivisionError as e :
    print(e.__class__.__name__)
    print(e)


except NameError:
    print('colocu uma str')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)

except Exception:
    print('Error desconhecido')


    



    
print('Continuar')
