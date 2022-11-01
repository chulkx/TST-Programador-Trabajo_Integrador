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

    def cargar_propiedad():
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
