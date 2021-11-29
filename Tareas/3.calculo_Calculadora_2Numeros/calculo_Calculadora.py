print("_________________________________________")
print("|                                       |")
print("|         \U0001F606 Hola binvenido \U0001F606           |")         ##emojis en unicode borrar + y agregar 3 0.
print("|                      Att:Joseph T.    |")
print("_________________________________________")

print("En este programa podras hacer diferentes calculos matematicos:")
print("Como **sumar**, **restar**, **multiplicar**  y **dividir** entre dos numeros, es facil")
print()
print("1.Primero intoduce el número de la operación que deseas realizar:")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División, puedes probar con 0")
print("5.Salir")
print()

operacion = int(input("Introdusca aquí el numero de la operación que desea realizar: "))
print("\n" * 40)##Para imprimir la canataidad de espacios que quiera


if operacion==1:
    print("Muy bien \U0001F4AA haz elijido la opción de sumar")
    print()
    print("Introduce los números que vas a evaluar")
    number1 = float(input("Introduce el primer número: "))
    number2 = float(input("Introduce el segundo número: "))
    suma=(number1+number2)
    print()
    number1=str(number1)
    number2=str(number2)
    print("El resultado de la suma de "+ number1+ " + " +number2+" es: ---- ", suma, " ----")
    print("lo haz hecho muy bien\U0001F60E")
    print("CHAO  \U0001F44B")



elif operacion==2:
    print("Muy bien\U0001F4AA haz elijido la opción de restar")
    print()
    print("Introduce los números que vas a evaluar")
    number1 = float(input("Introduce el primer número: "))
    number2 = float(input("Introduce el segundo número: "))
    resta = (number1 - number2)
    print()
    number1 = str(number1)
    number2 = str(number2)
    print("El resultado de la resta de " + number1 + " - " + number2 + " es: ---- ", resta, " ----")
    print("lo haz hecho muy bien\U0001F60E")
    print("CHAO  \U0001F44B")

elif operacion==3:
    print("Muy bien\U0001F4AA haz elijido la opción de multiplicar")
    print()
    print("Introduce los números que vas a evaluar")
    number1 = float(input("Introduce el primer número: "))
    number2 = float(input("Introduce el segundo número: "))
    multiplicar = (number1 * number2)
    print()
    number1 = str(number1)
    number2 = str(number2)
    print("El resultado de la multiplicación de " + number1 + " *" + number2 + " es: ---- ", multiplicar, " ----")
    print("lo haz hecho muy bien\U0001F60E")
    print("CHAO  \U0001F44B")

elif operacion==4:
    print("Muy bien\U0001F4AA haz elijido la opción de dividir")
    print()
    print("Introduce los números que vas a evaluar")
    number1 = float(input("Introduce el primer número: "))
    number2 = float(input("Introduce el segundo número: "))
    if number2 != 0:
        dividir = (number1 / number2)
        print()
        number1 = str(number1)
        number2 = str(number2)
        print("El resultado de la división de " + number1 + " / " + number2 + " es: ---- ", dividir, " ----")
        print("lo haz hecho muy bien\U0001F60E")
        print("CHAO  \U0001F44B")
    else:
        print()
        print("\U0001F630 \U00002622ERROR\U00002622: No puedes dividir numeros entre 0")

else:
    print("Gracias por entrar \U0001F60E")
    print("CHAO  \U0001F44B")
