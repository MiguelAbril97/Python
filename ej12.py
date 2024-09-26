from clases import rectangulo

r1=rectangulo(9,15)
r2=rectangulo(46,25)

area = r1.getArea()
perimetro = r1.getPerimetro()


print("Area y perímetro del primer rectángulo "+str(area)+" "+str(rectangulo.getPerimetro(r1)))
print("Area y perímetro del segundo rectángulo "+str(rectangulo.getPerimetro(r2))+str(rectangulo.getPerimetro(r2)))