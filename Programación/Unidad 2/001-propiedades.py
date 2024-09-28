class Gato:
    def _int_(self):
        self.altura = None
        self.edad = None
        self.peso = None
        self.nombre = None
        
    def maulla(self,numero):
        cadena = "Miau "*numero
        print(cadena)
    
    def estufera(self):
        print("ffffffffff")
        
        
gato1 = Gato ()
gato1.nombre = "Misifu"
print("El nombre del gato es",gato1.nombre)

