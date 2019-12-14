
#print("¿Contra que pokemon quieres luchar?")
#print("Bulbasaur")
#print("Squirtle")
#print("Charmander")

#vida_de_tu_pokemon = 100
#eleccion_de_pokemon = print(input("Elige un pokemon: "))

#if eleccion_de_pokemon == "Charmander":
#    print("Empieza el combate contra Charmander")


##Estableciendo objetos##
pokemon_elegido = input("¿Contra que pokemon quieres luchar? (Bulbasaur/Squirtle/Charmander)")
vida_Pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

##Eleccion de enemigo##
if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = 7

elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    ataque_enemigo = 12
## Bucle de ataques ##

while vida_Pikachu > 0 and vida_enemigo > 0:

    ###Ataques de Pikachu###
    ataque_elegido = input("¿Que ataque quieres elegir? (Chispazo / Bola voltio)")
    if ataque_elegido == "Chispazo":
        vida_enemigo -= 10
        print("Tu enemigo ha sufrido 10 puntos de daño")
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
        print("Tu enemigo ha sufrido 12 puntos de daño")
    print("la vida de {} es de {} puntos".format(pokemon_elegido,vida_enemigo))

### terminar_turno = input("¿Has terminado tu turno?(Si/No)")
###  while terminar_turno == "Si":
### if terminar_turno == "No":
### print("No te quedan mas acciones en este turno")


        ### Ataques de los enemigos ###

    if pokemon_elegido == "Squirtle":
        vida_Pikachu -= ataque_enemigo
        print("{} ataca provocandote unos {} puntos de daño".format(pokemon_elegido,ataque_enemigo))
    elif pokemon_elegido == "Charmander":
        vida_Pikachu -= ataque_enemigo
        print("{} ataca provocandote unos {} puntos de daño".format(pokemon_elegido,ataque_enemigo))
    elif pokemon_elegido == "Bulbasaur":
        vida_Pikachu -= ataque_enemigo
        print("{} ataca provocandote unos {} puntos de daño".format(pokemon_elegido,ataque_enemigo))
    print("la vida de Pikachu es de {}".format(vida_Pikachu))

##Mensaje de muerte de pokemon ##

if vida_Pikachu <= 0:
    print("Pikachu ha sido derrotado")
else:
    print("{} ha sido derrotado".format(pokemon_elegido))

print("El combate ha terminado")

