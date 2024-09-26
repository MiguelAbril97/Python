class persona ():
    def __init__(self,nombre="",edad=0):
        self.nombre=nombre
        self.edad=edad

class rectangulo ():
    
    def __init__(self, ancho=0, altura=0):
        self.ancho=ancho
        self.altura=altura
    
    def getArea(self):
        return self.ancho*self.altura
    
    def getPerimetro(self):
        return (2*self.ancho)+(2*self.altura)
    
class estudiante ():
    def __init__(self,nombre="", edad = 0, curso="" ):
        self.nombre=nombre
        self.edad=edad
        self.curso=curso

class cuentaBancaria():
    def __init__(self, titular="", saldo=0):
           self.titular=titular
           self.saldo=saldo
           
    def depositar(self, dinero=0):
        self.saldo+=dinero
    
    def retirar(self, dinero=0):
        self.saldo-=dinero

class coche():
    def __init__(self, marca="", modelo=""):
        self.marca=marca
        self.modelo=modelo
    
    def mostrarInfo(self):
        print("Marca: "+str(self.marca)+"\nModelo: "+str(self.modelo))
        
#Ejercicio 16 Clase animal e hijas

class Animal (): 
    def __init__(self, nombre=""):
        self.nombre=nombre
    
    def hablar(self):
        print("Mensaje genérico")

class perro(Animal):
    def __init__(self):
        super().__init__("perro")
        
    def hablar(self):
        print("Guau")
        
class gato(Animal):
    def __init__(self):
        super().__init__("gato")
        
    def hablar(self):
        print("Miau")
        
#Ej17 clases FiguraGeometrica y derivadas

class FiguraGeometrica():
    def __init__(self, base=0, altura=0):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura

class rectangulo(FiguraGeometrica):
    def __init__(self, base=0, altura=0):
        super().__init__(base, altura)
        
    def area(self):
        return super().area()

class triangulo(FiguraGeometrica):
    def __init__(self, base=0, altura=0):
        super().__init__(base, altura)
        
    def area(self):
        return (self.base*self.altura)/2
    
#Ej 18 clase Vehiculo y derivadas

class Vehiculo():

    def __init__(self, marca="", modelo=""):
        self.marca=marca
        self.modelo=modelo
        
    def mostrarInfo(self):
        print("Marca: "+str(self.marca)+"\nModelo: "+str(self.modelo))
        

class bici(Vehiculo):
    def __init__(self, marca="", modelo=""):
        super().__init__(marca, modelo)
        
    def cambiarCadena(self):
        print("La cadena se ha cambiado")

class coche(Vehiculo):
    def __init__(self, marca="", modelo=""):
        super().__init__(marca, modelo)
    
    def pasarIYV(self):
        print("El coche ha pasado la revisión")
        

#Ej19 clase InstrumentoMusical y derivados

class  InstrumentoMusical():
    def __init__(self, nombre=""):
        self.nombre=nombre
    
    def tocar(self):
        print("turururu")
    
class piano(InstrumentoMusical):
    
    def __init__(self, nombre=""):
        super().__init__("piano")
    
    def tocar(self):
        print("Suena claro de luna")
    
class guitarra(InstrumentoMusical):
    def __init__(self, nombre=""):
        super().__init__("guitarra")
    
    def tocar(self):
        print("Nothing else matters")
        
#Ej20 clase Empleado y derivados

class empleado():
    def __init__(self, nombre="", salario=0):
        self.nombre=nombre
        self.salario=salario
    
    def calcular_salrio_anual(self):
        return self.salario*12


class programador(empleado):
    def __init__(self, nombre="", salario=0,posicion = "programador"):
        super().__init__(nombre, salario)
        
        
    def aumentarSalario(self, aumento=0):
        self.salario+=aumento
    
    def disminuirSalario(self,cambio=0):
        self.salario-=cambio
        
        