def print_welcome_messaje():
    print("_________________________________________")
    print("|                                       |")
    print("|         \U0001F606 HOLA BIENVENIDO \U0001F606          |")  ##emojis en unicode borrar + y agregar 3 0.
    print("|                      Att:Joseph T.    |")
    print("_________________________________________")
    print("En este programa podras hacer diferentes calculos matematicos:")
    print("Como **sumar**, **restar**, **multiplicar**  y **dividir** entre dos numeros, es facil")
    print()


def menu_óption_messaje():
    print("Intoduce el número de la operación que deseas realizar:")
    print("0. Salir ")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División, puedes probar con 0")
    print()
    operacion = int(input("Introdusca aquí el numero de la operación que desea realizar: "))

    print("\n" * 40)  ##Para imprimir la canataidad de espacios que quiera
    return operacion


def number_operation():
    print("Introduce los números que vas a evaluar")
    number_1 = float(input("Introduce el primer número: "))
    number_2 = float(input("Introduce el segundo número: "))
    print("\n" * 3)
    return number_1, number_2


def suma_operation(f_number, s_number):
    print("Muy bien \U0001F4AA haz elijido la opción de sumar\n")
    suma = (f_number + s_number)
    print("El resultado de la suma de " + str(f_number) + " + " + str(s_number) + " es: ---- ", suma, " ----")
    print("lo haz hecho muy bien\U0001F60E")


def resta_operation(f_number, s_number):
    print("Muy bien\U0001F4AA haz elijido la opción de restar\n")
    resta = (f_number - s_number)
    print("El resultado de la resta de " + str(f_number) + " - " + str(s_number) + " es: ---- ", resta, " ----")
    print("lo haz hecho muy bien\U0001F60E")


def multiplicacion_operation(f_number, s_number):
    print("Muy bien\U0001F4AA haz elijido la opción de multiplicar\n")
    multiplicar = (f_number * s_number)
    print("El resultado de la multiplicación de " + str(f_number) + " *" + str(s_number) + " es: ---- ", multiplicar,
          " ----")
    print("lo haz hecho muy bien\U0001F60E")


def fin():
    if operacion != 1 and operacion != 2 and operacion != 3 and operacion != 4:
        print("Gracias por entrar \U0001F60E")
        print("CHAO  \U0001F44B")
        exit()


def divsion_operation(f_number, s_number):
    print("Muy bien\U0001F4AA haz elijido la opción de dividir\n")
    if s_number != 0:
        dividir = (f_number / s_number)
        print("El resultado de la división de " + str(f_number) + " / " + str(s_number) + " es: ---- ", dividir,
              " ----")
        print("lo haz hecho muy bien\U0001F60E")

    else:
        print()
        print("\U0001F630 \U00002622ERROR\U00002622: No puedes dividir numeros entre 0")


while True:
    print_welcome_messaje()
    operacion = menu_óption_messaje()
    fin()
    number_1, number_2 = number_operation()
    if operacion == 1:
        suma_operation(number_1, number_2)

    elif operacion == 2:
        resta_operation(number_1, number_2)
    elif operacion == 3:
        multiplicacion_operation(number_1, number_2)
    elif operacion == 4:
        divsion_operation(number_1, number_2)
