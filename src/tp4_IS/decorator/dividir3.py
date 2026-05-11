from decorador import Decorador


class Dividir3(Decorador):

    def obtener_valor(self):
        return self.componente.obtener_valor() / 3