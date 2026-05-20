from abc import ABC, abstractmethod



# Clase base de la cadena

class Handler(ABC):

    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, number):
        pass



# Handler de números primos

class PrimeHandler(Handler):

    def is_prime(self, n):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True

    def handle(self, number):

        if self.is_prime(number):
            print(f"{number} → consumido por PRIME")

        elif self.next_handler:
            self.next_handler.handle(number)



# Handler de números pares

class EvenHandler(Handler):

    def handle(self, number):

        if number % 2 == 0:
            print(f"{number} → consumido por EVEN")

        elif self.next_handler:
            self.next_handler.handle(number)



# Handler por defecto

class DefaultHandler(Handler):

    def handle(self, number):
        print(f"{number} → NO consumido")



# Construcción de la cadena

prime_handler = PrimeHandler()
even_handler = EvenHandler()
default_handler = DefaultHandler()

prime_handler.set_next(even_handler).set_next(default_handler)



# Procesar números del 1 al 100

for number in range(1, 101):
    prime_handler.handle(number)