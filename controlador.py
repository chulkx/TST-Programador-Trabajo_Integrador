from ast import operator
import modelo as mo
from rich import print
from rich.console import Console
from rich.table import Table

consola = Console()

def cargar_propiedad():
    a = True
    con = mo.Conectar()

    consola.print('Ingrese la informacion necesaria para cargar una propiedad.\n')

    consola.print('Ingrese el ID del tipo correspondiente: ', style=('bold blue'))
    tipos = con.listar_tipos()
    tabla = Table(title='Tipo de Propiedad')
    tabla.add_column("ID Tipo", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("NOMBRE", style="magenta")
    for t in tipos:
        tabla.add_row(str(t[0]), str(t[1]))
    consola.print(tabla)

    while a:
        try:
            tipo = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    consola.print('Ingrese el ID del estado correspondiente: ', style=('bold blue'))
    estados = con.listar_estado()
    for e in estados:
        consola.print('ID: ', e[0] ,' ---> ', e[1])
    a = True
    while a:
        try:
            estado = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    consola.print('Ingrese el ID de la operatoria correspondiente: ', style=('bold blue'))
    operaciones = con.listar_operatoria()
    for o in operaciones:
        consola.print('ID: ', o[0] ,' ---> ', o[1])
    a = True
    while a:
        try:
            operatoria = int(input('->'))
            a = False
        except:
            consola.print('Dato incorrecto')

    consola.print('Ingrese el ID del propietario correspondiente: ', style=('bold blue'))
    propietarios = con.listar_propietario()
    for p in propietarios:
        consola.print('ID: ', p[0] ,' ---> ', p[1])
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


def cargar_propietario():
    con = mo.Conectar()
    consola.print("Nombre:",style=("bold blue"))
    nombre = input("-> ")
    print("\n")
    consola.print("Dirección:",style=("bold blue"))
    direccion = input("-> ")
    print("\n")
    consola.print("Contacto:",style=("bold blue"))
    contacto = input("->")
    nuevo_propietario = mo.Propietario(0, nombre, direccion, contacto)
    con.cargar_propietario(nuevo_propietario)
    con.conexion.close()

    consola.print(f"'El Propietario '{nombre}' fue ingresado con éxito.'")
    input("Presione ENTER para continuar")
    

def modif_propiedad():
    con = mo.Conectar()
    listar_propiedades()
    consola.print('Ingrese el ID de la Propiedad que desea modificar:', style='bold green')
    id_p = input('->')
    listar_propiedades_por_id(id_p)
    consola.print('Ingrese el numero de campo que desea modificar:', style='bold green')
    consola.print('Recuerde que no puede modificar el ID de la Propiedad', style='bold red')
    campo = int(input('->'))
    if campo == 2:
        campo_c = 'id_tipo'
        print(con.listar_tipos())
    elif campo == 3:
        campo_c = 'id_operatoria_comercial'
        print(con.listar_operatoria())
    elif campo == 4:
        campo_c = 'id_estado'
        print(con.listar_estado())
    elif campo == 5:
        campo_c = 'nombre'
    elif campo == 6:
        campo_c = 'direccion'
    elif campo == 7:
        campo_c = 'contacto'

    print('Ingrese el nuevo dato:')
    dato = input('->')
    con.modif_propiedad(campo_c, dato, id_p)




def eliminar_propiedad():
    consola.print("Ingrese el ID de la propiedad a eliminar: ",style=("bold blue"))
    id_p = input("->")
    con = mo.Conectar()
    con.eliminar_propiedad(id_p)
    
def listar_propiedades_por_id(id):
    con = mo.Conectar()
    listado = con.listar_propiedades_por_id(id)
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("1 - ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("2 - TIPO", style="magenta")
    tabla.add_column("3 - OPERATORIA", style="magenta")
    tabla.add_column("4 - ESTADO", style="magenta")
    tabla.add_column("5 - PROPIETARIO", style="magenta")
    tabla.add_column("6 - NOMBRE", style="magenta")
    tabla.add_column("7 - DIRECCION", style="magenta")
    tabla.add_column("8 - CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
    consola.print(tabla)


def listar_propiedades():
    con = mo.Conectar()
    listado = con.consulta_propiedades_tabla()
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("TIPO", style="magenta")
    tabla.add_column("OPERATORIA", style="magenta")
    tabla.add_column("ESTADO", style="magenta")
    tabla.add_column("PROPIETARIO", style="magenta")
    tabla.add_column("NOMBRE", style="magenta")
    tabla.add_column("DIRECCION", style="magenta")
    tabla.add_column("CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
        
    consola.print(tabla)
    input("Presiones ENTER para continuar")

def listar_propiedades_venta():
    con = mo.Conectar()
    listado = con.consulta_propiedades_venta()
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("TIPO", style="magenta")
    tabla.add_column("OPERATORIA", style="magenta")
    tabla.add_column("ESTADO", style="magenta")
    tabla.add_column("PROPIETARIO", style="magenta")
    tabla.add_column("NOMBRE", style="magenta")
    tabla.add_column("DIRECCION", style="magenta")
    tabla.add_column("CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
        
    consola.print(tabla)
    input("Presiones ENTER para continuar")

def listar_propiedades_alquiler():
    con = mo.Conectar()
    listado = con.consulta_propiedades_alquiler()
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("TIPO", style="magenta")
    tabla.add_column("OPERATORIA", style="magenta")
    tabla.add_column("ESTADO", style="magenta")
    tabla.add_column("PROPIETARIO", style="magenta")
    tabla.add_column("NOMBRE", style="magenta")
    tabla.add_column("DIRECCION", style="magenta")
    tabla.add_column("CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
        
    consola.print(tabla)
    input("Presiones ENTER para continuar")

def listar_propiedades_vendidas():
    con = mo.Conectar()
    listado = con.consulta_propiedades_vendidas()
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("TIPO", style="magenta")
    tabla.add_column("OPERATORIA", style="magenta")
    tabla.add_column("ESTADO", style="magenta")
    tabla.add_column("PROPIETARIO", style="magenta")
    tabla.add_column("NOMBRE", style="magenta")
    tabla.add_column("DIRECCION", style="magenta")
    tabla.add_column("CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
        
    consola.print(tabla)
    input("Presiones ENTER para continuar")

def listar_propiedades_alquiladas():
    con = mo.Conectar()
    listado = con.consulta_propiedades_alquiladas()
    tabla = Table(title='Propiedades', show_lines=True)
    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("TIPO", style="magenta")
    tabla.add_column("OPERATORIA", style="magenta")
    tabla.add_column("ESTADO", style="magenta")
    tabla.add_column("PROPIETARIO", style="magenta")
    tabla.add_column("NOMBRE", style="magenta")
    tabla.add_column("DIRECCION", style="magenta")
    tabla.add_column("CONTACTO", style="magenta")
    for l in listado:
        tabla.add_row(str(l[0]), str(l[1]), str(l[2]), str(l[3]), str(l[4]), str(l[5]), str(l[6]), str(l[7]))
        
    consola.print(tabla)
    input("Presiones ENTER para continuar")
