import modelo as mo
from rich import print
from rich.console import Console

consola = Console()

def cargar_propiedad():
    con = mo.Conectar()
    consola.print('Ingrese la informacion necesaria para cargar una propiedad.\n')
    consola.print("Nombre:",style=("bold blue"))
    nombre = input("-> ")
    print("\n")
    consola.print("Dirección:",style=("bold blue"))
    direccion = input("-> ")
    print("\n")
    consola.print("Contacto:",style=("bold blue"))
    contacto = input("->")
    print("\n")

    nueva_prop = mo.Propiedad(0, nombre, direccion, contacto )
    con.cargar_propiedad(nueva_prop)
    con.conexion.close()

    consola.print(f'La propiedad '{nombre}', ubicada en '{direccion}' fue ingresada con éxito.')
    input("Presione ENTER para continuar")



def modif_propiedad():
    pass

def eliminar_propiedad():
    pass

def listar_propiedades():
    pass

def listar_propiedades_venta():
    pass

def listar_propiedades_alquiler():
    pass

def listar_propiedades_vendidas():
    pass

def listar_propiedades_alquiladas():
    pass
