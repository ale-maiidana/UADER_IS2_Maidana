from ping_proxy import PingProxy


proxy = PingProxy()

print("Caso 1")
proxy.execute("192.168.1.10")

print("\nCaso 2")
proxy.execute("8.8.8.8")

print("\nCaso 3")
proxy.execute("192.168.0.254")