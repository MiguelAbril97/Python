num = int(input("Dame un numero y te doy el factorial: "))
calculo = 1
for i in range(1,num+1):
    calculo*=i

print("El factorial de "+str(num)+" es: "+str(calculo))