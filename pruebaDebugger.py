def sumar(a,b):
    suma = a+b
    return suma

def restar (a,b):
    resta= a-b
    return resta

def multiplicar (a,b):
    x=a*b
    return x

def dividir (a,b):
    x=a/b
    return x

for i in range (1,3):
    print(sumar(i,5))
    
for i in range (1,3):
    print(restar(i,5))
    
for i in range (1,3):
    print(multiplicar(i,5))
    
for i in range (1,3):
    print(dividir(i,5))
    
