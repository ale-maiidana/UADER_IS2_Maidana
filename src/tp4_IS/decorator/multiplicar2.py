from decorador import Decorador


class Multiplicar2(Decorador):

    def obtener_valor(self):
        return self.componente.obtener_valor() * 2