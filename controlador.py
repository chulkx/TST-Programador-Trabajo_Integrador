import modelo as mo
from rich import print
from rich.console import Console

consola = Console()

def cargar_propiedad():
    a = True
    con = mo.Conectar()

    consola.print('Ingrese la informacion necesaria para cargar una propiedad.\n')

    tipos = con.listar_tipos()
    for t in tipos:
        consola.print('ID: ', t[0] ,' ---> ', t[1])
        print('\n')
    consola.print('Ingrese el ID del tipo correspondiente: ', style=('bold blue'))
    while a:
        try:
            tipo = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    estados = con.listar_estado()
    for e in estados:
        consola.print('ID: ', t[0] ,' ---> ', t[1])
        print('\n')
    consola.print('Ingrese el ID del estado correspondiente: ', style=('bold blue'))
    a = True
    while a:
        try:
            estado = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    operaciones = con.listar_operatoria()
    for o in operaciones:
        consola.print('ID: ', t[0] ,' ---> ', t[1])
        print('\n')
    consola.print('Ingrese el ID de la operatoria correspondiente: ', style=('bold blue'))
    a = True
    while a:
        try:
            operatoria = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    propietarios = con.listar_propietario()
    for p in propietarios:
        consola.print('ID: ', t[0] ,' ---> ', t[1])
        print('\n')
    consola.print('Ingrese el ID del propietario correspondiente: ', style=('bold blue'))
    a = True
    while a:
        try:
            propietario = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    consola.print("Nombre:",style=("bold blue"))
    nombre = input("-> ")
    print("\n")
    consola.print("Dirección:",style=("bold blue"))
    direccion = input("-> ")
    print("\n")
    consola.print("Contacto:",style=("bold blue"))
    contacto = input("->")
    print("\n")

    nueva_prop = mo.Propiedad(0, tipo, estado, operatoria, propietario, nombre, direccion, contacto )
    con.cargar_propiedad(nueva_prop)
    con.conexion.close()

    consola.print(f"'La propiedad '{nombre}', ubicada en '{direccion}' fue ingresada con éxito.'")
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
