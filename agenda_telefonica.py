salida = False
agenda = dict()
while not salida:
    accion_usuario = input("¿Que quieres hacer?(Añadir numero (A)/Consultar numero (C)/Salir (S)): ")
    #Añadir un numero
    if accion_usuario == "A":
        print("Añadir contacto nuevo")
        print("----------------------")
        nombre = input("Introduce un nombre:")
        numero = input("Introduce un numero de telefono:")
        agenda[nombre] = numero
    #Consultar un numero
    elif accion_usuario == "C":
        print("Consultar contacto existente")
        print("-----------------------------")
        contacto_consultar = input("Introduce el nombre del contacto:")
        print("El numero de telefono de {} es:".format(contacto_consultar))
        print((agenda[contacto_consultar]))
    #Salir
    elif accion_usuario == "S":
        salida = True

#EJERCICIO1
#Programa capaz de guardar y consultar nombres de amigos y años de nacimiento
#EJERCICIO2
#Programa que al decirle en nombre de un color devuelva la traduccion en ingles
#EJERCICIO3
#Crear un programa que cuente el numero de veces que aparece una palabra en una string
#EJERCICIO4
#Crea una funcion que muestre por pantalla un texto y tantas barritas de subrayado como larga sea la string