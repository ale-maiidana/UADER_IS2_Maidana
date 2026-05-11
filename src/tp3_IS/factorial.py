class Factorial:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def calcular(self, n):
        if n < 0:
            raise ValueError("No existe factorial de números negativos")
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)



if __name__ == "__main__":
    factorial = Factorial()

    try:
        numero = int(input("Ingrese un número entero: "))
        resultado = factorial.calcular(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError as e:
        print("Error:", e)