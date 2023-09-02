print("Ingresa el mensaje cifraado")
mensaje_cifrado = input()
print("Cuántas veces quieres mover la letra")
veces = int(input())

mensaje= ""

for i in range(0, len(mensaje_cifrado), 1):
    letra = mensaje_cifrado[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensaje += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensaje += nuevaLetra

print(mensaje)