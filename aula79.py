from itertools import count


c1 = count(8 , 8)
r2 = range(8,100, 8)

for i in c1:
    if i > 100:
        break

    print(i)


for i in r2:
    print(i)


