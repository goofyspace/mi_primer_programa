numeros_usuario = []


while len(numeros_usuario) < int(10):
    while not numeros_usuario.isdigit():
        numeros_introducidos = input("Mete un numero:")
        numeros_usuario.append(int(numeros_introducidos))
    print("NUMERO AÑADIDO")
    umeros_usuario = ""

print(numeros_usuario)