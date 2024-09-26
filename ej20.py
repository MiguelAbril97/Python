from clases import empleado, programador, limpieza

p1= empleado("Laura", 1300)
print("Salario anual de "+str(p1.nombre)+" es de: "+str(p1.calcular_salrio_anual()))

p2= programador("Pablo", 1350)
print("Salario anual de "+str(p2.nombre)+" es de: "+str(p2.calcular_salrio_anual()))
p2.disminuirSalario(100)
print("Salario anual de "+str(p2.nombre)+" es de: "+str(p2.calcular_salrio_anual()))

p3=limpieza("Jose", 1250, "mañana")
print("El trabajador "+str(p3.nombre)+" tiene horario de "+str(p3.horario))
p3.cambiarHorario("tardes")
print("El trabajador "+str(p3.nombre)+" tiene horario de "+str(p3.horario))

