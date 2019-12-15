

texto_usuario = input("Introduce un texto: ")

contador_mayusculas = 0

for item in texto_usuario:
    if item == item.upper() and item != " ":
        contador_mayusculas += 1

print("mayusculas = {}".format(contador_mayusculas))
