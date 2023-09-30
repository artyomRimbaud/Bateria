

# Ejercicio 1: ¿Es primo un número?

def es_primo(n):
    if n <= 1: return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def main1():
    num = int(input("Introduce un número entero: "))
    print(f"{num} es un número {'primo' if es_primo(num) else 'no primo'}.")


# Ejercicio 2: Primo siguiente

def primo_siguiente(n):
    n += 1
    while not es_primo(n): n += 1
    return n

def main2():
    num = int(input("Ingresa un número: "))
    print(f"El siguiente número primo después de {num} es {primo_siguiente(num)}.")


# Ejercicio 3: Mediana de tres valores

def mediana(a, b, c):
    return sorted([a, b, c])[1]

def main3():
    x, y, z = [float(input(f"Ingresa el número {i+1}: ")) for i in range(3)]
    print(f"La mediana de {x}, {y} y {z} es {mediana(x, y, z)}.")


# Ejercicio 4: Contraseña aleatoria

import random

def main4():
    print(f"Contraseña generada: {''.join(chr(random.randint(33, 126)) for _ in range(random.randint(7, 10)))}")


# Ejercicio 5: Calcular la hipotenusa

import math

def main5():
    cateto1, cateto2 = map(float, input("Ingresa las longitudes de los catetos separadas por espacio: ").split())
    print(f"La hipotenusa es: {math.sqrt(cateto1**2 + cateto2**2)}.")

