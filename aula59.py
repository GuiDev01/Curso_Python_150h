s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4, 5))
#s1.clear()
s1.discard('Olá mundo')
s1.discard('Luiz')

#print(s1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s2 ^ s1 

print(s3)