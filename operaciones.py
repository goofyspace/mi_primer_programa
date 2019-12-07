###Trabajamos con las operaciones booleanas, es decir operaciones logicas donde las respuestas solo pueden ser TRUE o FALSE
### Utilizamos el OR y el AND
### Cuando utilizamos el AND ambas opciones tienen que ser True para que el resultado sea TRUE, si una de las opciones es FALSE el resultado siempre sera FALSE
### Cuando utilizamos el OR solo basta con que una de las opciones sea TRUE para que el resultado sea TRUE
### Al igual que las operaciones convencionales las operaciones booleanas le dan prioridad a aquellas operaciones que esten entre parentesis

print("BIENVENIDO A LA HELADERIA")

saldo = 35
chocolate = 7
fresa = 10
vainilla = 36

print("Tu saldo es : {} " .format(saldo) )

te_apetece_un_helado=input("¿te apetece un helado?(si/no) ").upper()
dinero_helado=input("¿tienes dinero para un helado (si/No)? ")

if te_apetece_un_helado == "si" and dinero_helado == "si":
    print("estos son los precios de los helados")
    print("Chocolate : {}".format(chocolate))
    print("Fresa : {}".format(fresa))
    print("Vainilla : {}".format(vainilla))

else:
    print("Que pase un buen dia")

eleccion = input("¿que helado te apetece? ")

if eleccion == "Chocolate" and chocolate <= saldo:
    print("aqui tiene su helado")

else:
    print("No puede comprar ese helado")

if eleccion == "Fresa" and fresa <= saldo:
    print("aqui tiene su helado")

else:
    print("No puede comprar ese helado")

if eleccion == "Vainilla" and vainilla <= saldo:
    print("aqui tiene su helado")

else:
    print("No puede comprar ese helado")