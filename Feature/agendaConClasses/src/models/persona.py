

class Persona:
    def __init__(self, nombre, apellido, apodo,telefono,parentesco):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo=apodo
        self.telefono=telefono
        self.parentesco=parentesco

    def exportarContac(self):
        return {'nombre':self.nombre, 'apellido':self.apellido, 'apodo':self.apodo, 'telefono':self.telefono, 'parentesco':self.parentesco}



