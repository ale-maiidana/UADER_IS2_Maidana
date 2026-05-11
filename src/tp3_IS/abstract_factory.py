class Boton:
    def dibujar(self):
        pass


class Ventana:
    def abrir(self):
        pass

class BotonWindows(Boton):
    def dibujar(self):
        print("Botón estilo Windows")


class VentanaWindows(Ventana):
    def abrir(self):
        print("Ventana Windows")


class BotonLinux(Boton):
    def dibujar(self):
        print("Botón estilo Linux")


class VentanaLinux(Ventana):
    def abrir(self):
        print("Ventana Linux")

class UIFactory:
    def crear_boton(self):
        pass

    def crear_ventana(self):
        pass

class WindowsFactory(UIFactory):
    def crear_boton(self):
        return BotonWindows()

    def crear_ventana(self):
        return VentanaWindows()


class LinuxFactory(UIFactory):
    def crear_boton(self):
        return BotonLinux()

    def crear_ventana(self):
        return VentanaLinux()

if __name__ == "__main__":
    sistema = input("Ingrese sistema (windows/linux): ").lower()

    if sistema == "windows":
        factory = WindowsFactory()
    else:
        factory = LinuxFactory()

    boton = factory.crear_boton()
    ventana = factory.crear_ventana()

    boton.dibujar()
    ventana.abrir()