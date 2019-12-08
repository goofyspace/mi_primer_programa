
numero_inicial = 10

if numero_inicial == 10:
        print(int("10"))
        print("Este numero es par")
while numero_inicial > 0:
    numero_inicial -= 1
    print(numero_inicial)
    if  numero_inicial % 2 == 0:
        print("Este numero es par")
    else:
        print("Este numero es inpar")