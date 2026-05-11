class Factura:
    def mostrar(self):
        pass

class IVAResponsable(Factura):
    def mostrar(self):
        print("Factura IVA Responsable")


class IVANoInscripto(Factura):
    def mostrar(self):
        print("Factura IVA No Inscripto")


class IVAExento(Factura):
    def mostrar(self):
        print("Factura IVA Exento")

class FacturaFactory:

    @staticmethod
    def crear_factura(tipo):
        if tipo == "responsable":
            return IVAResponsable()
        elif tipo == "no_inscripto":
            return IVANoInscripto()
        elif tipo == "exento":
            return IVAExento()
        else:
            raise ValueError("Tipo de cliente inválido")
        
if __name__ == "__main__":
    tipo = input("Ingrese condición (responsable/no_inscripto/exento): ").lower()

    try:
        factura = FacturaFactory.crear_factura(tipo)
        factura.mostrar()
    except ValueError as e:
        print("Error:", e)