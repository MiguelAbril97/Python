from clases import cuentaBancaria

cuenta1=cuentaBancaria("Miguel", 4000)

print(cuenta1.saldo)

cuenta1.retirar(900)

print(cuenta1.saldo)

cuenta1.depositar(1200)

print(cuenta1.saldo)
