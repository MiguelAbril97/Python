import random
lista=[]
suma=0
for i in range (0,11):
    lista.append(random.randint(1,100))

for i in lista:
    suma+=i

suma = suma/len(lista)

print(str(suma))