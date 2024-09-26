from clases import estudiante

e1=estudiante("Julia", 19, "1 DAW")
e2 = estudiante ("Manuel", 23, "2 DAW")    
e3 = estudiante ("Marco", 16, "4 ESO")
e4 = estudiante ("Paula", 24, "2 DAM")

lista = [e1, e2, e3, e4]

for i in lista:
    print("Nombre: "+str(i.nombre)+ 
          "\nEdad: "+str(i.edad)+ "\nCurso: "+str(i.curso))