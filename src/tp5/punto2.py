
# Clase contenedora

class Cadena:

    def __init__(self, texto):
        self.texto = texto

    def iterador_directo(self):
        return IteradorDirecto(self.texto)

    def iterador_reverso(self):
        return IteradorReverso(self.texto)



# Iterator directo

class IteradorDirecto:

    def __init__(self, texto):
        self.texto = texto
        self.posicion = 0

    def hay_siguiente(self):
        return self.posicion < len(self.texto)

    def siguiente(self):
        caracter = self.texto[self.posicion]
        self.posicion += 1
        return caracter



# Iterator reverso

class IteradorReverso:

    def __init__(self, texto):
        self.texto = texto
        self.posicion = len(texto) - 1

    def hay_siguiente(self):
        return self.posicion >= 0

    def siguiente(self):
        caracter = self.texto[self.posicion]
        self.posicion -= 1
        return caracter



# Programa principal

cadena = Cadena("HOLA")


print("Recorrido directo:")
iterador1 = cadena.iterador_directo()

while iterador1.hay_siguiente():
    print(iterador1.siguiente())


print("\nRecorrido reverso:")
iterador2 = cadena.iterador_reverso()

while iterador2.hay_siguiente():
    print(iterador2.siguiente())