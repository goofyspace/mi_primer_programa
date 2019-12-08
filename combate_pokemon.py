
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
vida_de_Pikachu = 100
vida_de_enemigo = 0

##Eleccion de enemigo##
if pokemon_elegido == "Squirtle":
    vida_de_enemigo = 90

if pokemon_elegido == "Charmander":
    vida_de_enemigo = 80

if pokemon_elegido == "Bulbasaur":
    vida_de_enemigo = 100

## Bucle de ataques ##

while vida_de_Pikachu > 0 and vida_de_enemigo > 0:

    ###Ataques de Pikachu###
    ataque_elegido = input("¿Que ataque quieres elegir? (Chispazo / Bola voltio)")
    if ataque_elegido == "Chispazo":
        vida_de_enemigo -= 10
        print("Tu enemigo ha sufrido 10 puntos de daño")
    if ataque_elegido == "Bola voltio":
        vida_de_enemigo -= 12
        print("Tu enemigo ha sufrido 12 puntos de daño")
    print("la vida de {} es de {} puntos".format(pokemon_elegido,vida_de_enemigo))

### terminar_turno = input("¿Has terminado tu turno?(Si/No)")
###  while terminar_turno == "Si":
### if terminar_turno == "No":
### print("No te quedan mas acciones en este turno")


        ### Ataques de los enemigos ###

    if pokemon_elegido == "Squirtle":
        vida_de_Pikachu -= 8
        print("Squirtle ataca provocandote unos 8 puntos de daño")
    if pokemon_elegido == "Charmander":
        vida_de_Pikachu -= 7
        print("Charmander ataca provocandote unos 7 puntos de daño")
    if pokemon_elegido == "Bulbasaur":
        vida_de_Pikachu -= 12
        print("Bulbasaur ataca provocandote unos 12 puntos de daño")
    print("la vida de Pikachu es de {}".format(vida_de_Pikachu))

##Mensaje de muerte de pokemon ##

if vida_de_Pikachu <= 0:
    print("Pikachu ha sido derrotado")
else:
    print("{} ha sido derrotado".format(pokemon_elegido))

print("El combate ha terminado")

#####MINUTO 16