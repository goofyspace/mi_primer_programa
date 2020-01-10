##programa que encuentre el numero mas grande entre 3 numeros
##programa que diga si un numero esta dentro de un rango
##programa que muestre de una lista de numeros solo los pares

#1
def numero_mayor(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3 > numero1 and numero3 > numero2:
        return numero3

print(numero_mayor(5,444,3))

#2

respuesta_rango = False
def numero_dentro_rango(numero_elegido,minimo,maximo):
    numero_rango = numero_elegido
    numero_minimo = minimo
    numero_maximo = maximo
    if  numero_rango > numero_minimo and numero_rango < numero_maximo:
        return "YES"
    else:
        return "NO"

print(numero_dentro_rango(11,7,10))

#3

def numeros_pares(lista_numeros):
    #####CONTINUAR