numero_elegido = int(input("Elige un numero: "))
contador = 11
resultado = 0

for item in range(1,11):
        contador -= 1
        resultado = contador * numero_elegido
        if resultado == resultado:
            print("{} x {} = {}".format(contador,numero_elegido,resultado))