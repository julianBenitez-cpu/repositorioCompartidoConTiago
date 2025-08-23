import random

"""
1)

n = 1
while n <= 10:
    print(n)
    n += 1"
"""
"""
2)

num = int(input("Introduce un número: "))
factorial = 1
contador = 1

while contador <= num:
    factorial *= contador
    contador += 1

print(f"El factorial de {num} es {factorial}")"
"""



numero_Oculto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_Oculto:
        print("Es mayor")
    elif intento > numero_Oculto:
        print("Es menor")
    else:
        print(f"GGs Adivinaste el número en {intentos} intentos.")
        adivinado = True
