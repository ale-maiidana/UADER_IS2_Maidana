avion = Avion("body", "2 alas", "2 turbinas", "tren")
class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión con:", ", ".join(self.partes))
class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("body")

    def construir_turbinas(self):
        self.avion.agregar_parte("2 turbinas")

    def construir_alas(self):
        self.avion.agregar_parte("2 alas")

    def construir_tren(self):
        self.avion.agregar_parte("tren de aterrizaje")

    def obtener_avion(self):
        return self.avion

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_avion(self):
        self.builder.construir_body()
        self.builder.construir_turbinas()
        self.builder.construir_alas()
        self.builder.construir_tren()
    
if __name__ == "__main__":
    builder = AvionBuilder()
    director = Director(builder)

    director.construir_avion()
    avion = builder.obtener_avion()

    avion.mostrar()