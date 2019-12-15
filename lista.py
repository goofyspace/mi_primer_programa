

####APUNTES### Los metodos son pequeñas funciones asociadas a una variable.Como por ejemplo el .format en las string

###APPEND , metodo utilizado para agregar un dato a una nueva lista


mi_lista = []
input_usuario = "Lo siguiente:"

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que deseas agregar a la lista de la compra?(Escribe FIN para salir): ").upper()

#largo_lista = len(mi_lista)
#indice_actual = 0

#while indice_actual < largo_lista:
    #print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    #indice_actual += 1
#print("Esta es la lista de la compra")

for item in mi_lista:
    print("Tienes que comprar {}".format(item))

print("Fin de la lista de la compra")