import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100) #Genera un número aleatorio entre 1 y 100
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de números!")
    print("El juego consiste en adivinar un número entre 1 y 100.")
    print("¡Intenta adivinarlo!")
    
    while not adivinado:
        adivinanza = input("Introduzca un numero del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza) #Lo estamos pasando de texto a entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(f"Felicidades has ganado! El numero secreto es {adivinanza}. Lo has adivinado en {intentos} intentos")
        else:
            print("Por favor, tiene que ser un número entre el 1 al 100.")

juego_adivinanza()