class Ping:

    def execute(self, ip):
        if ip.startswith("192."):
            for i in range(10):
                print(f"Ping a {ip} intento {i + 1}")
        else:
            print("Dirección IP no permitida")

    def executefree(self, ip):
        for i in range(10):
            print(f"Ping libre a {ip} intento {i + 1}")

            