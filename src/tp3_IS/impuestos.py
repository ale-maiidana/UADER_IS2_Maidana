class Impuestos:

    @staticmethod
    def calcular(base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        municipal = base_imponible * 0.012

        return base_imponible + iva + iibb + municipal


# Programa principal
if __name__ == "__main__":
    try:
        base = float(input("Ingrese el importe base imponible: "))
        total = Impuestos.calcular(base)
        print(f"Total con impuestos: {total}")
    except ValueError:
        print("Error: debe ingresar un número válido")