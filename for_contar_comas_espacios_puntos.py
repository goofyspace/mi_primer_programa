texto_contar = input("introduce un texto: ")

contador_puntos = 0
contador_comas = 0
contador_espacios = 0

puntos = "."
comas = ","
espacios = " "

for item in texto_contar:
    if item == puntos:
        contador_puntos += 1
    elif item == comas:
        contador_comas += 1
    elif item == espacios:
        contador_espacios += 1

print("Puntos: {}".format(contador_puntos))
print("Comas: {}".format(contador_comas))
print("Espacios: {}".format(contador_espacios))

