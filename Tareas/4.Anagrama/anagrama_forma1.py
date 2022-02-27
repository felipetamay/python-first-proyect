# prueba 1
# mensaje de bienvenida
#Metodo crear diccionarios y compararlos.

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
    print("'''Ingresa las palabras que deseas comparar'''")


# se  toma la primera palabra se separa en un diccionario.
def cuentaPrimeraPalabra():
    primera_palabra = input("Ingrese la primera palabra:__|")
    cuenta_pri_palabra = {}

    for i in primera_palabra:
        if i not in cuenta_pri_palabra:
            cuenta_pri_palabra[i] = 1

        else:
            cuenta_pri_palabra[i] += 1
    return cuenta_pri_palabra



# se toma segunda palabra se separa en un diccionario
def cuentaSegundaPalabra():
    segunda_palabra = input("Ingrese la segunda palabra:__ |")
    cuenta_seg_palabra = {}

    for i in segunda_palabra:
        if i not in cuenta_seg_palabra:
            cuenta_seg_palabra[i] = 1

        else:
            cuenta_seg_palabra[i] += 1
    return cuenta_seg_palabra


# Se toman los dccionearios y se comparan.
def comparacion():
    cuenta_pri_palabra = cuentaPrimeraPalabra()
    cuenta_seg_palabra = cuentaSegundaPalabra()

    if cuenta_pri_palabra == cuenta_seg_palabra:
        print(
            "\033[34mMuy bien\U0001F4AA \033[0m las palabras ingresadas \033[33mSI\033[0m son \033[33mANAGRAMA\033[0m\n")
    else:
        print("\033[34mLo lamento\U0001F625 \033[0m las palabras ingresadas \033[33mNO\033[0m son \033[33mANAGRAMA\033[0m\n")

#funcion para salir cuando se encunetra siclo wile
def salir():
    print("Quieres terminar o volver a repetir?")
    salir = int(input("Salir 0 o continuar 1\n:__|"))
    if salir == 0:
        print("Gracias por entrar \U0001F60E")
        exit()


while True:
    mensajeDeBienvenida()
    comparacion()
    salir()
