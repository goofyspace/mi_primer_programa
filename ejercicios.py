#EJERCICIO1
#Programa capaz de guardar y consultar nombres de amigos y años de nacimiento
#EJERCICIO2
#Programa que al decirle en nombre de un color devuelva la traduccion en ingles
#EJERCICIO3
#Crear un programa que cuente el numero de veces que aparece una palabra en una string
#EJERCICIO4
#Crea una funcion que muestre por pantalla un texto y tantas barritas de subrayado como larga sea la string
###########################################################################
###########################################################################

#EJERCICIO1
#Programa capaz de guardar y consultar nombres de amigos y años de nacimiento
nombres_años = dict()
salir = False

while not salir:
    accion = input("Agregar nombre y año de nacimiento(A)/Consultar nombre y año de nacimiento(C)/Salir(S)")
    if accion == "A" or accion == "a":
        print("Añadir nombre y año de nacimiento:")
        print("----------------------------------")
        nombre = input("Introduce un nombre:")
        año = input("Introduce el año de nacimiento")
        nombres_años[nombre] = año
    elif accion == "C" or accion == "c":
        print("Consultar año de nacimiento:")
        print("----------------------------")
        consulta = input("Introduce un nombre:")
        print(nombres_años[consulta])
    elif accion == "S" or accion == "s":
        salir = True

#EJERCICIO2
#Programa que al decirle en nombre de un color devuelva la traduccion en ingles
colores = {"rojo": "red", "amarillo": "yellow", "azul": "blue", "verde": "green", "negro": "black", "blanco": "white"}
salida = False

while not salida:
    color_traducir = input("¿Que color deseas traducir?: ")
    print(colores[color_traducir])
    volver_traducir = input("¿Deseas traducir otro color?(Si/No):")
    if volver_traducir == "SI" or volver_traducir == "si" or volver_traducir == "Si":
        pass
    else:
        salida = True
#EJERCICIO3
#Crear un programa que cuente el numero de veces que aparece una palabra en una string
