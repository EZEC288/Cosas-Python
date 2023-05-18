texto = input("Ingresa un Texto:")
letras = input("Ingresa 3 Letras separadas:").split()
for letras in letras:
    print(f"La letra '{letras}' aparece {texto.count(letras)} veces en el texto.")

    palabras = texto.split()
    print(f"En total hay {len(palabras)} palabras en el texto")

    primera_letra = texto[0]
    ultima_letra = texto[-1]
    print(f"La primera letra es '{primera_letra}' y la ultima letra es '{ultima_letra}'.")

    texto_inverso = texto[::-1]
    print(f"El texto en orden Inverso es: '{texto_inverso}'")

    if "python" in palabras:
        print("Si aparece la Palabra Python en el Texto")
    else:
        print("No aparece la Palabra Python en el Texto")

