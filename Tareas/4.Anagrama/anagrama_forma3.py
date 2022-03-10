# prueba 2
# Creación diccionario
#Metodo: Se crea un diccionario de a la z asignadole un valor numerico
#se covierte cada palabra en una lista
#se toma la lista y se remplaza por el valor numerico de la lista
#se hace reliza el procedimineto con la primera palabra holay la segunda palabra.
#Se comparan las dos listas ya ordenadas.

def mensajeDeBienvenida():
    print("                       \n                       ***Hola como estas***")
    print("                              Bienvenido")
    print("Aquí podras comparar dos palabras y ver si es anagrama o no es anagrama")
    print("Que es un anagrama:")
    print("   'Procedimiento que consiste en crear una palabra \n"
          "a partir de la reordenación de las letras de otra palabra'\n ")
    print("Ejemplo:")
    print("\033[34mR O M A  \033[0m")
    print("\033[34m  M   M O R A  \033[0m")
    print("\033[34m  A   O  \033[0m")
    print("\033[34m  R   R A M O\033[0m")
    print("\033[34m        R\033[0m")
    print("\033[34m        M\033[0m")
    print("\033[34m        O\033[0m\n")
    print("'''Ingresa las palabras que deseas comparar '''")


#>Se realiza el diccionario Alfabetico.
def ordenalfabetico():
    alfabeto={
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "ñ":15,
        "o":16,
        "p":17,
        "q":18,
        "r":19,
        "s":20,
        "t":21,
        "u":22,
        "v":23,
        "w":24,
        "x":25,
        "y":26,
        "z":27,
    }
#La palabra A se convierte en una lista
    primera_palabra = input("Ingrese la primera palabra:__|")
    palabraf=[]
    for i in primera_palabra:
        palabraf+=i

#Se le asigna el codigo a la lista de la palabara A
    codigos=[]
    for letra in palabraf:
        codigos.append(alfabeto[letra])
    ordenados=sorted(codigos)

#La palabra B se convierte en una lista
    segundaPalabra = input("Ingrese la segunda palabra:___|")
    palabrabf = []
    for i in segundaPalabra:
        palabrabf += i

# Se le asigna el codigo a la lista de la palabara B
    codigosb = []
    for letrab in palabrabf:
        codigosb.append(alfabeto[letrab])
    ordenadosb = sorted(codigosb)


#Se compara las listas ya ordenadas.
    if ordenadosb==ordenados:
        print(
            "\033[34mMuy bien\U0001F4AA \033[0m las palabras ingresadas \033[33mSI\033[0m son \033[33mANAGRAMA\033[0m\n")
    else:
        print("\033[34mLo lamento\U0001F625 \033[0m las palabras ingresadas \033[33mNO\033[0m son \033[33mANAGRAMA\033[0m\n")

def salir():
    print("Quieres terminar o volver a repetir?")
    salir = int(input("Salir 0 o continuar 1 :__|"))
    if salir != 1:
        print("Gracias por entrar \U0001F60E")
        exit()

while True:
  mensajeDeBienvenida()
  ordenalfabetico()
  salir()



