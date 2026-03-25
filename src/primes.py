# Programa que calcula y muestra los números primos entre 1 y 500

# Recorremos todos los números en el rango indicado
for num in range(1, 501):

    # Asumimos inicialmente que el número es primo
    is_prime = True

    # Verificamos si tiene divisores distintos de 1 y de sí mismo
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Si sigue siendo primo, lo mostramos
    if is_prime and num > 1:
        print(num)