from componente import Componente


class Pieza(Componente):

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("   " * nivel + f"Pieza: {self.nombre}")