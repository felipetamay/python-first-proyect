# prueba 2
# mensaje de bienvenida
#Metodo: Se toma le restan las letras de la primera palabra a la segunda
#luego se cunta las letras restantes de la palabra b si da 0 es anagrama por que las letras de a estan en b
#se corrige error ya que si las letras de a estan en b pero b es mas laraga tambien se tomara por anagrama
#Se corrige contando cuantas letras hay en la primera y segunda palabra estas deberan ser igules.
#presenta algunos errores


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


# estructura del programa
def Desarrollo():
    palabraA = input("Para esto.... \nIngrese la primera palabra:__|")
    palabraB = input("Ingrese la segunda palabra:___|")

#Cuenta de letras que tiene B
    cuentasletrasB = 0
    for i in palabraB:
        cuentasletrasB += 1


# Quitar letras de de la primera palabra en la segunda palabra
    for i in range(len(palabraA)):
        palabraB = palabraB.replace(palabraA[i], "")
    palabraBNueva=palabraB



#Cuenta de letras que tien A
    cuentasletrasA=0
    for i in palabraA:
        cuentasletrasA+=1

#Cueanta de las letras de la palabra B sin la palabra A.
    cuentaspalabraBNueva=0
    for i in palabraB:
        cuentaspalabraBNueva+=1


#Comparacion y determinacion de anagrama.
    if cuentaspalabraBNueva == 0 and cuentasletrasA==cuentasletrasB:
        print("\033[34mMuy bien\U0001F4AA \033[0m las palabras ingresadas \033[33mSI\033[0m son \033[33mANAGRAMA\033[0m\n")
    else:
        print("\033[34mLo lamento\U0001F625 \033[0m las palabras ingresadas \033[33mNO\033[0m son \033[33mANAGRAMA\033[0m\n")



def salir():
    print("Quieres terminar o volver a repetir?")
    salir = int(input("Salir 0 o continuar 1 :__|"))
    if salir == 0:
        print("Gracias por entrar \U0001F60E")
        exit()

while True:
  mensajeDeBienvenida()
  Desarrollo()
  salir()
