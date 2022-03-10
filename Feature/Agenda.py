#Ejercicio Agenda
#Nombre
#Apellido
#Telefono

personas = []
def bienvenida():
    print("\n"*40)
    print("_________________________________________")
    print("| 8:17 PM                 \U0001F4F6  \U0001F4F6 \U0001F50B 85%  |")
    print("| \U0001F50D    Buscar contacto               \U000022EE  |") #\U0001F50D Icono buscar
    print("|                                       |")
    print("|                                       |")
    print("|    _______________        \33[32m \U0001F4DE \33[0m        |")
    print("|                                       |")
    print("|    _______________        \33[32m \U0001F4DE \33[0m        |")
    print("|                                       |")
    print("|    _______________        \33[32m \U0001F4DE \33[0m        |")
    print("|                                       |")
    print("|                                       |")
    print("|    ___________________  \33[34m   .....\33[0m      |")
    print("|    ___________________     \33[34m.....\33[0m      |")
    print("|    ___________________       \33[34m.\33[0m        |")
    print("|                                       |")
    print("|     \U00002605            \U0001F551          \U0001F465       |")
    print("| Favoritos    Recientes   Contactos    |")
    print("|_______________________________________|")
    print("|      \U000025B6            \U000025CF          \U000025A1        |")
    print("|_______________________________________|")

def opciones():

    while True:
        print("\nElija la opción a la que desea accceder:")
        print("1. \U0001F464+ Crear contacto nuevo")
        print("2. \U0001F50D Buscar contactos")
        print("3. \U0001F4DA Agenda de contactos")
        print("0. SALIR")
        opcion_entrada = input("Ingrese la opcion elegida:____:")
        print("\n" * 3)

        if opcion_entrada=="1":
            crear()
        if opcion_entrada=="2":
            buscar()
        if opcion_entrada=="3":
            lista()
        if opcion_entrada=="0":
            salir()
        else:
            print("\n"*5)
            print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")
def crear():
    print("\n\U0001F464+ Crear contacto nuevo")
    nombre = input("Ingrese el nombre del contacto:_____:")
    apellido = input("Ingrese el apellido del contacto:____:")
    while True:
        try:
            telefono = int(input("Ingrese el telefono:____:"))
            break
        except ValueError:
            print("El dato ingresado no es un numero telefonico\n")

    parentesco = input("(ninguno, papa, mama...) Ingrese el parentresco:____:")
    persona = {
        'nombre': nombre.lower(),
        'apellido': apellido.lower(),
        'telefono':telefono,
        'parentesco':parentesco
    }
    personas.append(persona)

    while True:
      print()
      pausa=input("Para ingresar OTRO CONTACTO envia \033[34m (1)\033[0m o MENÚ \033[34m (2)\033[0m :___:")
      if pausa=='1':
        crear()
      elif pausa=='2':
        bienvenida()
        opciones()
      else:
        print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")
        input()

def terminoOp():
    print("Ahora envia", "\033[34m (1) \033[0m", "para ir al MENÚ o", "\033[34m (0)\033[0m", " para SALIR")
    listaRegre = input("Ingresa tu eleccion:___|")
    if listaRegre == "1":
      bienvenida()
      opciones()
    if listaRegre == "0":
            salir()
    else:
        print("\n" * 40)
        print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")

def lista():
    listaOrganizada=sorted(personas, key=lambda nombresor: nombresor['nombre'])

    for i in listaOrganizada:
        print('Nombre:', i["nombre"].capitalize(),i["apellido"].capitalize())
        print('Telefono:',"\33[32m\U0001F4DE\33[0m", i["telefono"])
        print('Parentesco:', i["parentesco"].capitalize())
        print()
    if personas == []:
        print("\33[31m''''NO HAY CONTACTOS REGISTRADOS''''\33[0m \n")
    while True:
        terminoOp()

def termibuscar():
    print("Para intentar de nuevo envia \033[34m (1)\033[0m o MENÚ \033[34m (2)\033[0m  para SALIR \033[34m (0)\033[0m\n")
    intnuevo = input("Ingrese su opcion:__:")
    if intnuevo == "1":
        buscar()
    if intnuevo == "2":
        bienvenida()
        opciones()
    if intnuevo == "0":
        salir()
    else:
        print("\n" * 5)
        print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")

def buscar():
    if personas == []:
        print("\33[31m''''NO HAY CONTACTOS REGISTRADOS''''\33[0m \n")
        while True:
            terminoOp()

    print("Aquí podra buscar el contacto ya sea por el nombre, apellido,telefono o parentesco Registrado")
    busqueda=input("Ingrese la info del contacto que desea buscar:_____:")
    print()
    for dato in personas:

        if busqueda==dato["nombre"] or busqueda==str(dato["telefono"]) or busqueda==dato["apellido"] or busqueda==dato["parentesco"] or busqueda==dato["nombre"].capitalize() or busqueda==dato["apellido"].capitalize() or busqueda==dato["parentesco"].capitalize():
            print("Nombre:", dato["nombre"].capitalize(), dato["apellido"].capitalize())
            print('Telefono:',"\33[32m\U0001F4DE\33[0m", dato["telefono"])
            print('Parentesco:', dato["parentesco"].capitalize())
            print()

    termibuscar()

    if busqueda!=dato["nombre"]:
        print("\n **El dato ingresado no esta en los registros**")
        termibuscar()


    print("\U0001F464+ Crear contacto nuevo")

def salir():
    print()
    print("Gracias por entrar \U0001F60E")
    exit()

bienvenida()
opciones()
