from numero import Numero
from sumar2 import Sumar2
from multiplicar2 import Multiplicar2
from dividir3 import Dividir3


numero = Numero(6)

print("Valor original:")
print(numero.obtener_valor())


suma = Sumar2(numero)

print("\nSumando 2:")
print(suma.obtener_valor())


multiplicacion = Multiplicar2(suma)

print("\nMultiplicando por 2:")
print(multiplicacion.obtener_valor())


division = Dividir3(multiplicacion)

print("\nDividiendo por 3:")
print(division.obtener_valor())