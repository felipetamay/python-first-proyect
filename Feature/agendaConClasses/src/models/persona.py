

class Persona:
    def __init__(self, nombre, apellido, apodo,telefono,parentesco,correo,birthay):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo=apodo
        self.telefono=telefono
        self.parentesco=parentesco
        self.correo=correo
        self.birthay=birthay

    def exportarContac(self):
        return {'nombre':self.nombre, 'apellido':self.apellido, 'apodo':self.apodo, 'telefono':self.telefono, 'parentesco':self.parentesco, 'correo':self.correo,'birthay':self.birthay}



