
# Clase Subject

class EmisorIDs:

    def __init__(self):
        self.observers = []

    def suscribir(self, observer):
        self.observers.append(observer)

    def emitir(self, id_emitido):

        print(f"\nID emitido: {id_emitido}")

        for observer in self.observers:
            observer.actualizar(id_emitido)



# Clase Observer

class Observer:

    def __init__(self, nombre, id_esperado):
        self.nombre = nombre
        self.id_esperado = id_esperado

    def actualizar(self, id_emitido):

        if id_emitido == self.id_esperado:
            print(f"{self.nombre} → ID coincidente encontrado")



# Programa principal

emisor = EmisorIDs()


# Crear observers
obs1 = Observer("Observer1", "AB12")
obs2 = Observer("Observer2", "ZX90")
obs3 = Observer("Observer3", "QWER")
obs4 = Observer("Observer4", "TY55")


# Suscribir observers
emisor.suscribir(obs1)
emisor.suscribir(obs2)
emisor.suscribir(obs3)
emisor.suscribir(obs4)


# Emitir IDs
ids = [
    "AB12",
    "AAAA",
    "ZX90",
    "BBBB",
    "QWER",
    "CCCC",
    "TY55",
    "DDDD"
]

for identificador in ids:
    emisor.emitir(identificador)