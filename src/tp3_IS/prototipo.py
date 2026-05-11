import copy

class Prototipo:

    def clonar(self):
        return copy.deepcopy(self)

class Avion(Prototipo):
    def __init__(self, modelo, capacidad):
        self.modelo = modelo
        self.capacidad = capacidad

    def mostrar(self):
        print(f"Modelo: {self.modelo}, Capacidad: {self.capacidad}")

if __name__ == "__main__":
    avion1 = Avion("Boeing 737", 180)

    avion2 = avion1.clonar()
    avion3 = avion2.clonar()

    avion1.mostrar()
    avion2.mostrar()
    avion3.mostrar()

    print("¿Son el mismo objeto?", avion1 is avion2)