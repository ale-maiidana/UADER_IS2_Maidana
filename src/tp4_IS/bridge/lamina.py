class Lamina:

    def __init__(self, espesor, ancho, tren):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = tren

    def fabricar(self):

        print(f"Espesor: {self.espesor}")
        print(f"Ancho: {self.ancho}")
        print(self.tren.producir())