import random

from palabras import palabras
from ahorcado import dibujos


def iniciar_juego():
    palabra_secreta = random.choice(palabras)
    palabra_oculta = ["_" for letra in palabra_secreta]

    vidas = 6
    letras_usadas = []

    print("\n================================")
    print("       JUEGO DEL AHORCADO")
    print("================================")

    while vidas > 0 and "_" in palabra_oculta:

        print(dibujos[6 - vidas])
        print("\nPalabra:", " ".join(palabra_oculta))
        print("Vidas restantes:", vidas)
        print("Letras utilizadas:", ", ".join(letras_usadas))

        letra = input("\nIngresa una letra: ").strip().upper()

        if len(letra) != 1:
            print("Error: debes ingresar solamente una letra.")
            continue

        if not ("A" <= letra <= "Z"):
            print("Error: solamente se permiten letras de A a Z.")
            continue

        if letra in letras_usadas:
            print("Ya utilizaste esa letra. Intenta con otra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra_secreta:
            print("¡Correcto! La letra está en la palabra.")

            for posicion in range(len(palabra_secreta)):
                if palabra_secreta[posicion] == letra:
                    palabra_oculta[posicion] = letra

        else:
            print("Letra incorrecta. Pierdes una vida.")
            vidas -= 1

    print(dibujos[6 - vidas])

    if "_" not in palabra_oculta:
        print("\n¡FELICIDADES! ¡GANASTE!")
        print("La palabra era:", palabra_secreta)
    else:
        print("\n¡HAS PERDIDO!")
        print("La palabra correcta era:", palabra_secreta)


def main():
    while True:
        iniciar_juego()

        print("\n================================")
        print("       FIN DE LA PARTIDA")
        print("================================")
        print("1. Jugar nuevamente")
        print("2. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            print("\n¡Comencemos una nueva partida!")
        elif opcion == "2":
            print("\nGracias por jugar al Ahorcado. ¡Hasta pronto!")
            break
        else:
            print("\nOpción inválida. El programa finalizará.")
            break


if __name__ == "__main__":
    main()
