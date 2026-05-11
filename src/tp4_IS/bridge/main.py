from lamina import Lamina
from tren_5m import Tren5m
from tren_10m import Tren10m


tren5 = Tren5m()
tren10 = Tren10m()

lamina1 = Lamina(0.5, 1.5, tren5)
lamina2 = Lamina(0.5, 1.5, tren10)

print("Producción 1")
lamina1.fabricar()

print("\nProducción 2")
lamina2.fabricar()