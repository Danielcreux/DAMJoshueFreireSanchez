class animal:

    def __init__(self,nombre=None,patas=4):
        self.nombre=nombre
        self.patas=patas
        self.tipo="Can"

x = animal("Max",2)
y = animal("Hugo",5)

print (x.nombre,x.patas, x.tipo)
print( y.nombre,y.patas, y.tipo)
