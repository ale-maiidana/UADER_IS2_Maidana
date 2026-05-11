class Hamburguesa:
    def entregar(self):
        pass
class Mostrador(Hamburguesa):
    def entregar(self):
        print("Entrega en mostrador")


class Retiro(Hamburguesa):
    def entregar(self):
        print("Retiro por el cliente")


class Delivery(Hamburguesa):
    def entregar(self):
        print("Entrega por delivery")

class HamburguesaFactory:

    @staticmethod
    def crear_hamburguesa(tipo):
        if tipo == "mostrador":
            return Mostrador()
        elif tipo == "retiro":
            return Retiro()
        elif tipo == "delivery":
            return Delivery()
        else:
            raise ValueError("Tipo de entrega inválido")
        
if __name__ == "__main__":
    tipo = input("Ingrese tipo de entrega (mostrador/retiro/delivery): ").lower()

    try:
        hamburguesa = HamburguesaFactory.crear_hamburguesa(tipo)
        hamburguesa.entregar()
    except ValueError as e:
        print("Error:", e)