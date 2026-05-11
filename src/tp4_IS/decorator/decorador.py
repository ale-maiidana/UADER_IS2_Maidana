class Decorador:

    def __init__(self, componente):
        self.componente = componente

    def obtener_valor(self):
        return self.componente.obtener_valor()