import mysql.connector
from rich import print

class Conectar():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                db = 'inmobiliaria'
            )
        except mysql.connector.Error as error_ocurrido:
            print('Error en la conexion, error: ', error_ocurrido)

    def cargar_propiedad(self, propiedad):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = 'INSERT INTO propiedad values(null, %s, %s, %s)'
            data = (
                propiedad.getIdProp(),
                propiedad.getTipo(),
                propiedad.getEstado(),
                propiedad.getOperatoria(),
                propiedad.getPopietario(),
                propiedad.getNombre(),
                propiedad.getDireccion(),
                propiedad.getContacto()
            )
        pass

    def modif_propiedad():
        pass

    def eliminar_propiedad():
        pass

    def consulta_propiedades():
        pass

    def consulta_propiedades_venta():
        pass

    def consulta_propiedades_alquiler():
        pass

    def consulta_propiedades_vendidas():
        pass

    def consulta_propiedades_alquiladas():
        pass

class Propiedad():
    def __init__(self, id_propiedad, tipo, estado, operatoria, propietario, nombre, direccion, contacto):
        self.id_propiedad = id_propiedad
        self.tipo = tipo
        self.estado = estado
        self.operatoria = operatoria
        self.propietario = propietario
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto

    def getIdProp(self):
        return self.id_propiedad
    def getTipo(self):
        return self.tipo
    def getEstado(self):
        return self.estado
    def getOperatoria(self):
        return self.operatoria
    def getPopietario(self):
        return self.propietario
    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getContacto(self):
        return self.contacto

    def setIdProp(self,id_propiedad):
        self.id_propiedad = id_propiedad
    def setTipo(self,tipo):
        self.tipo = tipo
    def setEstado(self,estado):
        self.estado = estado
    def setOperatoria(self,operatoria):
        self.operatoria = operatoria
    def setPropietario(self,propietario):
        self.propietario = propietario
    def setNombre(self,nombre):
        self.nombre = nombre
    def setDireccion(self,direccion):
        self.direccion = direccion
    def setContacto(self,contacto):
        self.contacto = contacto

class Estado():
    def __init__(self,id_estado, nombre):
        self.id_estado = id_estado
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_estado)+' '+self.nombre

    def getIdEstado(self):
        return self.id_estado
    def getNombre(self):
        return self.nombre

    def setIdEstado(self,id_estado):
        self.id_estado = id_estado
    def setNombre(self,nombre):
        self.nombre = nombre

class Tipo():
    def __init__(self,id_tipo, nombre):
        self.id_tipo = id_tipo
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_tipo)+' '+self.nombre

    def getIdTipo(self):
        return self.id_tipo
    def getNombre(self):
        return self.nombre

    def setIdTipo(self,id_tipo):
        self.id_tipo = id_tipo
    def setNombre(self,nombre):
        self.nombre = nombre

class Operatoria():
    def __init__(self,id_op, nombre):
        self.id_operatoria = id_op
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_operatoria)+' '+self.nombre

    def getIdOperatoria(self):
        return self.id_operatoria
    def getNombre(self):
        return self.nombre

    def setIdOperatoria(self,id_op):
        self.id_operatoria = id_op
    def setNombre(self,nombre):
        self.nombre = nombre

class Propietario():
    def __init__(self,id_propietario, nombre, direccion, contacto):
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto

    def __str__(self) -> str:
        return str(self.id_propietario)+' '+self.nombre

    def getIdTipo(self):
        return self.id_propietario
    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getContacto(self):
        return self.contacto

    def setIdTipo(self,id_propietario):
        self.id_propietario = id_propietario
    def setNombre(self,nombre):
        self.nombre = nombre
    def setDireccion(self, direccion):
        self.direccion = direccion
    def setContacto(self, contacto):
        self.contacto = contacto