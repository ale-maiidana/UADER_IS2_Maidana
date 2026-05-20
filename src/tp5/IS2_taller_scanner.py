import os

#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------

"""State class: Base State class"""
class State:

    def scan(self):

        # Barrido normal
        self.pos += 1

        if self.pos == len(self.stations):
            self.pos = 0

        print("Sintonizando... Estación {} {}".format(
            self.stations[self.pos],
            self.name
        ))

        # Barrido de memorias
        print("Memorias guardadas:")

        for memoria in self.radio.memorias:
            print("{} -> {} {}".format(
                memoria["nombre"],
                memoria["frecuencia"],
                memoria["banda"]
            ))


#*--------------------------------------------------------------------
# Estado AM
#*--------------------------------------------------------------------
class AmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):

        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


#*--------------------------------------------------------------------
# Estado FM
#*--------------------------------------------------------------------
class FmState(State):

    def __init__(self, radio):

        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):

        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


#*--------------------------------------------------------------------
# Clase Radio
#*--------------------------------------------------------------------
class Radio:

    def __init__(self):

        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        # Estado inicial
        self.state = self.fmstate

        # Memorias
        self.memorias = [
            {"nombre": "M1", "banda": "FM", "frecuencia": "95.5"},
            {"nombre": "M2", "banda": "AM", "frecuencia": "650"},
            {"nombre": "M3", "banda": "FM", "frecuencia": "102.3"},
            {"nombre": "M4", "banda": "AM", "frecuencia": "810"}
        ]

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


#*--------------------------------------------------------------------
# Programa principal
#*--------------------------------------------------------------------
if __name__ == "__main__":

    os.system("clear")

    print("\nCrea un objeto radio y almacena las siguientes acciones")

    radio = Radio()

    actions = (
        [radio.scan] * 3 +
        [radio.toggle_amfm] +
        [radio.scan] * 3
    )

    actions *= 2

    print("\nRecorre las acciones ejecutando la acción")

    for action in actions:
        action()
        print()