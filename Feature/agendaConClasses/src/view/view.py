from typing import Any
from ..models.persona import Persona

#Aqui se colocan los textos principales del programa
#De aqui a destacar se usan dos decoraciones para los textos
#La primera al modificacion es para el color de y negrilla de texto
#Negrilla: \33[1;30m negrila negro \33[0m__Finalizar la negrrilla
#color: \33[(numero)m numero define lel color
#la segund modificacion es el el uso de el uso de emetes y iconos
#los codigos se copian de unicode y se modican deacuerdo a la necesidad Ejemplo:U+1F4DE simbolo telefono->modi ->U0001F4DE


class View:
    def infoDeLaAplicacion(self):
        print("\n"*4)
        print("Este programa SIMULA el proceso de una agenda telfonica")
        print("Aquí podra realizar diferentes acciones que encontraria en una agenda telefonica")
        print("Como crear contactos, exportar, caragar(en diferentes tipos de archivos Json,xml) entre entras.")
        print("Para cargar los datos, los archivos estan creados comn el nombre" ,"'hola'", "por defecto")
        print("Pero puedes crear y guardar los arvos que quieras")
        print("                     \33[31mVAMOS INTENTALO \33[0m")

    def selecccionMenu(self):
        print("\n\33[1;30m","Escriba y envíe la opción a la que desea accceder:","\33[0m")
        print("1. \U0001F464+ Crear contacto nuevo.")
        print("2. \U0001F50D Buscar contactos.")
        print("3. \U0001F5D8 Cargar contactos (JSON).")
        print("4. \U00002191 Exportar contactos(JSON).")
        print("5. \U0001F5D8 Cargar contactos (XML).")
        print("6. \U00002191 Exportar contactos(XML).")
        print("7. \U0000232B Eliminar contacto.")
        print("8. \U0001F4DA Agenda de contactos.")
        print("0. SALIR\n")
        return int(input("\33[1;30mIngrese la opcion elegida:____:\33[0m"))
        print("\n" * 3)


    def bienvenida(self):

        print("_________________________________________")
        print("| 8:17 PM                 \U0001F4F6  \U0001F4F6 \U0001F50B 85%  |")
        print("| \U0001F50D    Buscar contacto               \U000022EE  |")  # \U0001F50D Icono buscar
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
        print("|      \33[36m\U000025B6\33[0m             \33[36m\U000025CF\33[0m         \33[36m\U000025A1\33[0m        |")
        print("|_______________________________________|")


    def datosPersona(self):
        print()
        nombre:Any=str(input("Ingrese la \33[1;30mnombre\33[0m del contacto:__|"))
        apellido:Any = str(input("Ingrese el \33[1;30mapellido\33[0m del contacto:__|"))
        apodo :Any=str(input("Ingrese el \33[1;30mapodo\33[0m del contacto:__|: "))
        while True:
            try:
                telefono:Any=int(input("Ingrese el \33[1;30mtelefono\33[0m del contacto:___|"))
                break
            except ValueError:
                print("El dato ingresado \33[31mNO\33[0m es un numero telefonico\33[31m\U000026A0\33[0m\n")

        parentesco:Any=str(input("Ingrese el \33[1;30mparentesco\33[0m del contacto:__|"))

        return Persona(nombre,apellido,apodo,telefono,parentesco)


    def personaCredaCorrectamente(self):

        print("\nLa \33[33mPERSONA\33[0m a sido creada correctamente \33[33m\U0000263A\33[0m\n")


    def crearNueva(self):
        pausa = input("Para ingresar OTRO CONTACTO envia \033[34m (1)\033[0m o MENÚ \033[34m (2)\033[0m :___:")
        return pausa


    def menssError(self):
        print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")


    def menssNoTel(self):
        print("El numero ingresado no es un numero Telefonico \33[31m\U000026A0\33[0m")


    def nombreCargaJson(self):
      return str(input("Ingrese el nombre con el que esta guardado el archivo:__|"))


    def nombreExportJson(self):
      return str(input("Ingrese el nombre con el quiere guardar el archivo:__|"))



    def menssCorect(self):
        print("\n\33[33m\U0000263A\33[0mLa \33[33mLISTA\33[0m a sido creada correctamente \33[33m\U0000263A\33[0m\n")


    def mensSalir(self):
        print("\nGracias por entrar")
        print("Sin embrago te recomendamos cargar los contactos si no lo haz hecho")
        salida=input("Para ingresar a cagar contactos con Json \033[34m (3)\033[0m con Xml \033[34m (5)\033[0m o salir definitivamente\033[34m (0)\033[0m :___:")
        return salida


    def terminoOp(self):
        print("Ahora envia", "\033[34m (1) \033[0m", "para ir al MENÚ o", "\033[34m (0)\033[0m", " para SALIR")
        listaRegre = input("Ingresa tu eleccion:___|")
        return listaRegre


    def busqueda(self):
        print("Aquí podra buscar el contacto ya sea por el nombre, apellido,telefono o parentesco Registrado")
        busqueda = input("Ingrese la info del contacto que desea buscar:_____:")
        print()
        return busqueda


    def datoNoRegistrado(self):
        print("\n **El dato ingresado no esta en los registros**")


    def terminarBusqueda(self):
        print("Para intentar de nuevo envia \033[34m (1)\033[0m o MENÚ \033[34m (2)\033[0m  para SALIR \033[34m (0)\033[0m\n")
        intnuevo = input("Ingrese su opcion:__:")
        return intnuevo


    def eliminarContacto(self):
        print("Aquí podra eliminar contactos ya sea con el nombre, apellido,telefono o parentesco Registrado")
        eliminar= input("Ingrese la info del contacto que desea eliminar:_____:")

        print()
        return eliminar


    def terminarEliminacion(self,):
        print("Para eliminar otro contacto envia \033[34m (1)\033[0m o MENÚ \033[34m (2)\033[0m  para SALIR \033[34m (0)\033[0m\n")
        intnuevo = input("Ingrese su opcion:__:")
        return intnuevo


    def eliminacioCorecta(self):
        print("\33[31mHa sido eliminado CORRECTAMNETE\33[0m\n")


    def continuar(self):
        input("Pulsa enter para continuar:_|")


    def vacio(self):
        print("la entrada esta vacia intente nuevente")