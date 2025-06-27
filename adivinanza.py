
import random

print(" ¡Bienvenido al juego: Adivina el número secreto!")
print("Estoy pensando en un número del 1 al 10.")
print("Tienes 3 intentos para adivinarlo. ¡Buena suerte!\n")


numero_secreto = random.randint(1, 10)


intentos_maximos = 3
intentos = 0

while intentos < intentos_maximos:
    try:
        adivinanza = int(input(f"Intento {intentos + 1}/{intentos_maximos}. Ingresa tu número: "))

        if adivinanza < 1 or adivinanza > 10:
            print(" El número debe estar entre 1 y 10. Intenta de nuevo.\n")
            continue

        intentos += 1

        if adivinanza == numero_secreto:
            print(f" ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
            break
        elif adivinanza < numero_secreto:
            print(" El número secreto es mayor. Intenta de nuevo.\n")
        else:
            print(" El número secreto es menor. Intenta de nuevo.\n")

    except ValueError:
        print(" Entrada no válida. Por favor, escribe un número entero.\n")


if intentos == intentos_maximos and adivinanza != numero_secreto:
    print(f" Lo siento, no adivinaste el número. Era {numero_secreto}. ¡Sigue practicando!")


print("meh")