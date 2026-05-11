from decorador import Decorador


class Sumar2(Decorador):

    def obtener_valor(self):
        return self.componente.obtener_valor() + 2