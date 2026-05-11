from componente import Componente


class Subconjunto(Componente):

    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):

        print("   " * nivel + f"Subconjunto: {self.nombre}")

        for componente in self.componentes:
            componente.mostrar(nivel + 1)