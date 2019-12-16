numero_elegido = int(input("Elige un numero: "))
contador_while = 0
resultado = 0
tabla = [int(5),int(6),int(7),int(8),int(9),int(10),int(11),int(12),int(13),int(14),int(15)]

while contador_while < len(tabla):
    for item in tabla:
        contador_while += 1
        if contador_while > 0:
            resultado = item * numero_elegido
            print("{} x {} = {}".format(item,numero_elegido,resultado))