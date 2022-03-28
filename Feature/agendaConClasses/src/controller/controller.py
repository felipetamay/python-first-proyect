import json
import xml.etree.cElementTree as ET
from datetime import date
from xml.etree.ElementTree import parse
from ..models.persona import Persona
from ..view.view import View

#el programa contiene la simulacion de un telefono en relacion con
#l agenda, telefonica, aqui se pueden relizar diferentes acciones de simulacion.
#Aqui (controller) se maneja la estructura principal del programa.
#Fecha y hora real
#muestra quien esta cumplindo años
#validacion de maxima edad con fecha actual


class Controller:
    def __init__(self):
        self.opcionElegida=0
        self.opVista = View()
        self.persona=Persona(nombre="",apellido="",apodo="",telefono=0,parentesco="", correo="", birthay="")
        self.contactos=[]
        self.contactoMos=[]
        self.diaA = int(format(date.today().day))
        self.mesA = int(format(date.today().month))
        self.fechas = [self.diaA,self.mesA]


    def terminarOpC(self):
        listaRegre = self.opVista.terminoOp()

        if listaRegre == "1":
            self.desarrolloMenu()
        if listaRegre == "0":
            self.salir()
        else:
            print("\n" * 40)
            print("\U000026A0\33[31mOPCIÓN INVALIDA\33[0m\U000026A0\n")



    def desarrolloMenu(self):


        self.opVista.infoDeLaAplicacion()
        while self.desarrolloMenu != 0:
            self.binevenida = self.opVista.bienvenida()
            for i in self.contactoMos:
                fecha = [i["birthay"][0], i["birthay"][1]]
                if fecha == self.fechas:
                    print("FELICITACIONES", i["nombre"].capitalize(), "estas cumpliendo años")

            while True:
                try:
                    self.opcionElegida = self.opVista.selecccionMenu()

                    break
                except ValueError:
                    self.opVista.menssError()
            if self.opcionElegida == 1:
                self.crearContacto()
            if self.opcionElegida == 2:
                self.buscarContacto()
            if self.opcionElegida == 3:
                self.cargarJson()
            if self.opcionElegida == 4:
                self.exportarJson()
            if self.opcionElegida == 5:
                self.eliminarContacto()
            if self.opcionElegida == 6:
                self.listaDeContactos()
            if self.opcionElegida == 0:
                self.salir()



    def crearContacto(self):
        persona=self.opVista.datosPersona()
        self.contactos.append(persona)
        self.contactoMos.append(persona.exportarContac())
        self.opVista.personaCredaCorrectamente()

        while True:
            pausa = self.opVista.crearNueva()

            if pausa=="1":
               self.crearContacto()
            if pausa=="2":
               self.desarrolloMenu()
            if pausa!="1" or pausa!="2":
                self.opVista.menssError()


    def exportarJson(self):
       nombreArchivo=self.opVista.nombreExportJson()
       if nombreArchivo == "":
           self.opVista.vacio()
           self.opVista.continuar()
           self.desarrolloMenu()
       listaAGuardar=[]
       for persona in self.contactos:
            listaAGuardar.append(persona.exportarContac())

       with open(f"data/{nombreArchivo}.json", "w") as fp:
           json.dump(listaAGuardar, fp)

       self.opVista.menssCorect()
       self.opVista.continuar()

    def cargarJson(self):
        print("PARA CARGAR por defecto ingresa HOLA")
        nombreCargaJson = self.opVista.nombreCargaJson()

        try:
            with open(f"data/{nombreCargaJson}.json", "r") as fp:
                data = json.load(fp)
            for persona in data:
                self.contactos.append(
                    Persona(
                        nombre=persona["nombre"],
                        apellido=persona["apellido"],
                        apodo=persona["apodo"],
                        telefono=persona["telefono"],
                        parentesco=persona["parentesco"],
                        correo=persona["correo"],
                        birthay=persona["birthay"]

                    )
                )
            for persona in self.contactos:
                self.contactoMos.append(persona.exportarContac())

            self.opVista.menssCorect()
            self.opVista.continuar()
        except Exception as e:
            self.opVista.menssError()
            self.opVista.continuar()

    def cargarXml(self):
        nombreArchivo=self.opVista.nombreCargaJson()
        try:
            datos = parse("data/" + nombreArchivo + ".xml")
            #print(datos)

            #for item in datos.iterfind("Persona"):
               # print(item)

            for item in datos.iterfind('Persona'):
                contactos = {"nombre": item.findtext('nombre'), "apellido": item.findtext('apellido'),"apodo": item.findtext('apodo'), "telefono": item.findtext('telefono'),"parentesco": item.findtext('parentesco')}
                #print(item.findtext('nombre'))
                # print(contactos)
                # print(self.contactoMos)
                self.contactoMos.append(contactos)
            self.opVista.menssCorect()
            self.opVista.continuar()

                # print(self.contactoMos)
        except Exception as e:
            self.opVista.menssError()
            self.opVista.continuar()

    def terminarEliminacion(self):
        intnuevo=self.opVista.terminarEliminacion()
        if intnuevo == "1":
            self.eliminarContacto()
        if intnuevo == "2":
            self.desarrolloMenu()
        if intnuevo == "0":
            self.salir()
        else:
            print("\n" * 5)
            self.opVista.menssError()
            self.terminarEliminacion()



    def eliminarContacto(self):

        if  self.contactoMos== []:
            print("\33[31m''''NO HAY CONTACTOS REGISTRADOS''''\33[0m \n")
            while True:
                self.terminarOpC()

        eliminar=self.opVista.eliminarContacto()


        for dato in self.contactoMos:
            if eliminar == dato["nombre"].lower() or eliminar == str(dato["telefono"]).lower() or eliminar == dato["apellido"].lower() or eliminar == dato["parentesco"].lower() or eliminar == dato["apodo"].capitalize() or eliminar == dato["apellido"].capitalize() or eliminar== dato["parentesco"].capitalize():

                dato.clear()

                print("              ",eliminar.capitalize())
        self.contactoMos = [elemento for elemento in self.contactoMos if elemento]
        self.opVista.eliminacioCorecta()
        self.terminarEliminacion()




    def listaDeContactos(self):

        listaOrganizada = sorted(self.contactoMos, key=lambda nombresor: nombresor['nombre'])

        for i in listaOrganizada:
            print('Nombre:', i["nombre"].capitalize(), i["apellido"].capitalize())
            print('Apodo:', i["apodo"].capitalize())
            print('Telefono:', "\33[32m\U0001F4DE\33[0m", i["telefono"])
            print('Parentesco:', i["parentesco"].capitalize())
            print('Correo:', i["correo"])
            print("telefono","Dia",i["birthay"][0],"Mes:",i["birthay"][1],"Año",i["birthay"][2])
            print()
        if self.contactoMos == []:
            print("\33[31m''''NO HAY CONTACTOS REGISTRADOS''''\33[0m \n")
        while True:
            self.terminarOpC()


    def buscarContacto(self):

        if  self.contactoMos== []:
            print("\33[31m''''NO HAY CONTACTOS REGISTRADOS''''\33[0m \n")
            while True:
                self.terminarOpC()

        busqueda=self.opVista.busqueda()

        for dato in self.contactoMos:

            if busqueda == dato["nombre"].lower() or busqueda == str(dato["telefono"]).lower() or busqueda == dato["apellido"].lower() or busqueda == dato["parentesco"].lower() or busqueda == dato["apodo"].capitalize() or busqueda == dato["apellido"].capitalize() or busqueda== dato["parentesco"].capitalize():
                print('Nombre:', dato["nombre"].capitalize(), dato["apellido"].capitalize())
                print('Apodo:', dato["apodo"].capitalize())
                print('Telefono:', "\33[32m\U0001F4DE\33[0m", dato["telefono"])
                print('Parentesco:', dato["parentesco"].capitalize())
                print('Correo:', dato["correo"])
                print("telefono", "Dia", dato["birthay"][0], "Mes:", dato["birthay"][1], "Año", dato["birthay"][2])
                print()
        self.terminarBusqueda()

    def salir(self):
        salir=self.opVista.mensSalir()
        if salir==3:
            self.exportarJson()
        else:
            exit()
    def terminarBusqueda(self,):
        intnuevo=self.opVista.terminarBusqueda()
        print(intnuevo)
        if intnuevo == "1":
            self.buscarContacto()
        if intnuevo == "2":
            self.desarrolloMenu()
        if intnuevo == "0":
            self.salir()
        else:
            print("\n" * 5)
            self.opVista.menssError()
            self.terminarBusqueda()
