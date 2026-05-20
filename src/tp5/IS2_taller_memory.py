import os

#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*--------------------------------------------------------------------

class Memento:

    def __init__(self, file, content):

        self.file = file
        self.content = content


class FileWriterUtility:

    def __init__(self, file):

        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):

        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:

    def __init__(self):

        # Lista de estados
        self.history = []

    def save(self, writer):

        # Guardar máximo 4 estados
        if len(self.history) == 4:
            self.history.pop(0)

        self.history.append(writer.save())

    def undo(self, writer, version):

        if version < len(self.history):

            # Recuperar desde el final
            index = -(version + 1)

            writer.undo(self.history[index])

        else:
            print("No existe esa versión")


#*--------------------------------------------------------------------
# Programa principal
#*--------------------------------------------------------------------

if __name__ == '__main__':

    os.system("cls" if os.name == "nt" else "clear")

    print("Crea un objeto que gestionará versiones anteriores")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")


    print("\nSe graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content)
    caretaker.save(writer)


    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content)
    caretaker.save(writer)


    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content)
    caretaker.save(writer)


    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content)
    caretaker.save(writer)


    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content)
    caretaker.save(writer)


    #--------------------------------------------------------------
    # Recuperar estados
    #--------------------------------------------------------------

    print("\nUNDO(0) -> último estado guardado")
    caretaker.undo(writer, 0)
    print(writer.content)


    print("\nUNDO(1) -> estado anterior")
    caretaker.undo(writer, 1)
    print(writer.content)


    print("\nUNDO(2) -> dos estados atrás")
    caretaker.undo(writer, 2)
    print(writer.content)


    print("\nUNDO(3) -> tres estados atrás")
    caretaker.undo(writer, 3)
    print(writer.content)