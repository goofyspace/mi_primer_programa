
texto_introducido = input("Introduce el texto para sacar las vocales: ")
vocales = ["a","e","i","o","u"]
vocales_texto = []

for item in texto_introducido:
    if item == vocales[0]:
        vocales_texto.append(item)
    elif item == vocales[1]:
        vocales_texto.append(item)
    elif item == vocales[2]:
        vocales_texto.append(item)
    elif item == vocales[3]:
        vocales_texto.append(item)
    elif item == vocales[4]:
        vocales_texto.append(item)

print("las vocales son las siguientes{}".format(vocales_texto))