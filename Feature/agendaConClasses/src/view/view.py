from typing import Any
from ..models.persona import Persona
from datetime import date
from datetime import datetime
#Aqui se colocan los textos principales del programa
#De aqui a destacar se usan dos decoraciones para los textos
#La primera al modificacion es para el color de y negrilla de texto
#Negrilla: \33[1;30m negrila negro \33[0m__Finalizar la negrrilla
#color: \33[(numero)m numero define lel color
#la segund modificacion es el el uso de el uso de emetes y iconos
#los codigos se copian de unicode y se modican deacuerdo a la necesidad Ejemplo:U+1F4DE simbolo telefono->modi ->U0001F4DE


class View:
    def __init__(self):
        self.corre1=[]
        self.dia=[]
        self.mes=[]
        self.year=[]
        self.diaA = int(format(date.today().day))
        self.mesA = int(format(date.today().month))
        self.yearA = int(format(date.today().year))
        self.telefono1=[]
        self.telefono2 = []
        self.cuentas=0



    def infoDeLaAplicacion(self):
        print("\n"*2)
        print("Este programa SIMULA el proceso de una agenda telfonica")
        print("Aquí podra realizar diferentes acciones que encontraria en una agenda telefonica")
        print("Como crear contactos, exportar, caragar(en diferentes tipos de archivos Json) entre entras.")
        print("Para cargar los datos, los archivos estan creados comn el nombre" ,"'hola'", "por defecto")
        print("Pero puedes crear y guardar los arvos que quieras")
        print("                     \33[31mVAMOS INTENTALO \33[0m")

    def selecccionMenu(self):
        print("\n\33[1;30m","Escriba y envíe la opción a la que desea accceder:","\33[0m")
        print("1. \U0001F464+ Crear contacto nuevo.")
        print("2. \U0001F50D Buscar contactos.")
        print("3. \U0001F5D8 Cargar contactos (JSON).")
        print("4. \U00002191 Exportar contactos(JSON).")
        print("5. \U0000232B Eliminar contacto.")
        print("6. \U0001F4DA Agenda de contactos.")
        print("0. SALIR\n")
        return int(input("\33[1;30mIngrese la opcion elegida:____:\33[0m"))



    def bienvenida(self):

        fecha=datetime.now().strftime('%d-%m-%Y')

        print("_________________________________________")
        print("| 8:17 PM  ",fecha,"   \U0001F4F6  \U0001F4F6 \U0001F50B 85%  |")
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
        parentesco: Any = str(input("Ingrese el \33[1;30mparentesco\33[0m del contacto:__|"))
        self.correo()
        correo=self.corre1[0]
        self.diaF()
        dia=self.dia[0]
        print(dia)
        self.mesF()
        mes=self.mes[0]
        print(mes)
        self.yearF()
        year=self.year[0]
        print(year)
        birthay=[dia,mes,year]

        self.corre1.clear()
        self.dia.clear()
        self.mes.clear()
        self.year.clear()
        self.tel()
        telF=self.telefono1[0]
        telefono=telF
        self.telefono1.clear()

        return Persona(nombre,apellido,apodo,telefono,parentesco,correo,birthay)
    def tel(self):
        while True:
            try:
                telefono=int(input("Ingrese el \33[1;30mtelefono\33[0m del contacto:___|"))
                if len(str(telefono))==10 and str(telefono)[0]=="3" and int(str(telefono)[1])<3:
                    self.telefono1.append(telefono)
                    return telefono
                else:
                    self.tel()
                    self.menssError()
                break

            except ValueError:
                print("El dato ingresado \33[31mNO\33[0m es un numero telefonico\33[31m\U000026A0\33[0m\n")
                self.tel()

    def correo(self):

        correoV=input("Ingrese el correo:")
        contarArroba=0
        contarpunto=0
        for i in correoV:
            if i=="@":
                contarArroba+=1
            if i==".":
                contarpunto+=1
        if contarArroba==1 and contarpunto>0:
            self.corre1.append(correoV)
        if contarArroba!=1 or contarpunto==0:
            self.menssError()
            self.correo()


    def diaF(self):
        try:
            diaT = int(input("ingrese el dia por favor:__|"))

            if diaT>31:
                self.menssError()
                self.diaF()
            self.dia.append(diaT)
            return diaT
        except ValueError:
            print("no es numero")
            self.diaF()


    def mesF(self):
        try:
            mesT = int(input("ingrese el mes por favor:__|"))

            if mesT>12:
                self.menssError()
                self.mesF()
            self.mes.append(mesT)
            return mesT
        except ValueError:
            print("no es numero")
            self.mesF()

    def yearF(self):
        try:
            yearT = int(input("ingrese el año por favor:__|"))

            if len(str(yearT))>4 or yearT>self.yearA or yearT<1900:
                self.menssError()
                self.yearF()
            self.year.append(yearT)
            return yearT
        except ValueError:
            print("no es numero")
            self.yearF()








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
        salida=input("Para ingresar a cagar contactos con Json \033[34m (3)\033[0m o salir definitivamente\033[34m (0)\033[0m :___:")
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