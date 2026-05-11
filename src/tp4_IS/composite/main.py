from pieza import Pieza
from subconjunto import Subconjunto


producto = Subconjunto("Producto Principal")


for i in range(1, 4):

    subconjunto = Subconjunto(f"Subconjunto {i}")

    for j in range(1, 5):
        pieza = Pieza(f"Pieza {i}.{j}")
        subconjunto.agregar(pieza)

    producto.agregar(subconjunto)


opcional = Subconjunto("Subconjunto Opcional")

for i in range(1, 5):
    opcional.agregar(Pieza(f"Opcional {i}"))

producto.agregar(opcional)


producto.mostrar()