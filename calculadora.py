
primer_numero = 0
segundo_numero = 0
repetir = "si"

## Preguntamos la operacion que quiere realizar ##
while repetir != "no":
        operacion = input("¿Que operacion quieres realizar?(sumar/restar/multiplicar/dividir): ")

## Pedimos los numeros con los que se va a realizar la operacion ##

        primer_numero = int(input("Primer numero: "))
        segundo_numero = int(input("Segundo numero: "))

### Mostramos resultado ###


        if operacion == "sumar":
                resultado_suma = float(primer_numero+segundo_numero)
                print("Resultado: {}".format(resultado_suma))


        elif operacion == "restar":
                resultado_resta = float(primer_numero-segundo_numero)
                print("Resultado: {}".format(resultado_resta))

        elif operacion == "multiplicar":
                resultado_multiplicacion = float(primer_numero * segundo_numero)
                print("Resultado: {}".format(resultado_multiplicacion))

        elif operacion == "dividir":
                resultado_division = float(primer_numero / segundo_numero)
                print("Resultado: {}".format(resultado_division))

        repetir = input("¿Desea realizar otra operacion(si/no)?: ")
