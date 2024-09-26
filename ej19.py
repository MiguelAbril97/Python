from clases import InstrumentoMusical, piano, guitarra

i=InstrumentoMusical("Tarareo")
print(i.nombre)
i.tocar()

i=piano()
print(i.nombre)
i.tocar()

i=guitarra()
print(i.nombre)
i.tocar()